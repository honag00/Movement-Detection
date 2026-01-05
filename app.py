"""
Flask application cho Camera IoT - Phát hiện chuyển động và streaming
"""
from flask import Flask, Response, render_template, jsonify, send_from_directory, request
import cv2
import threading
import time
import os
import numpy as np
from src import Camera, MotionDetector, config

app = Flask(__name__)

# Global variables
camera = None
motion_detector = None
current_frame = None
motion_detected = False
last_capture_time = 0
capture_cooldown = 2  # Thời gian chờ giữa các lần chụp ảnh (giây)
motion_window_start = 0  # Thời điểm bắt đầu cửa sổ 5 giây
motion_window_duration = 5  # Thời gian cửa sổ chụp ảnh (giây)
motion_window_active = False  # Có đang trong cửa sổ chụp ảnh không
frame_lock = threading.Lock()


def generate_frames():
    """
    Generator function để streaming video frames
    """
    global current_frame, motion_detected, last_capture_time, motion_window_start, motion_window_active
    
    while True:
        with frame_lock:
            camera_available = camera is not None and camera.is_opened
        
        # Nếu camera tắt, dừng stream hoàn toàn (không gửi frame nào)
        if not camera_available:
            time.sleep(0.5)
            continue
        
        success, frame = camera.read()
        if not success:
            time.sleep(0.1)
            continue
        
        # Phát hiện chuyển động
        if motion_detector:
            has_motion, processed_frame, contours = motion_detector.detect(frame)
            current_time = time.time()
            
            # Logic chụp ảnh trong cửa sổ 5 giây
            if has_motion:
                # Nếu chưa có cửa sổ hoạt động, bắt đầu cửa sổ mới
                if not motion_window_active:
                    motion_window_start = current_time
                    motion_window_active = True
                    print(f"Bắt đầu cửa sổ chụp ảnh 5 giây...")
                
                # Kiểm tra xem còn trong cửa sổ 5 giây không
                time_in_window = current_time - motion_window_start
                if time_in_window <= motion_window_duration:
                    # Trong cửa sổ 5 giây, chụp ảnh nếu đã qua cooldown
                    if (current_time - last_capture_time) > capture_cooldown:
                        filepath = motion_detector.save_capture(processed_frame)
                        print(f"Image saved: {filepath} (trong cửa sổ {time_in_window:.1f}s)")
                        last_capture_time = current_time
                else:
                    # Đã hết 5 giây, đóng cửa sổ
                    motion_window_active = False
                    print(f"Đã hết cửa sổ 5 giây, không chụp ảnh nữa")
            else:
                # Không có chuyển động
                if motion_window_active:
                    # Kiểm tra xem đã hết 5 giây chưa
                    time_in_window = current_time - motion_window_start
                    if time_in_window > motion_window_duration:
                        motion_window_active = False
                        print(f"Đã hết cửa sổ 5 giây, không có chuyển động, dừng chụp ảnh")
            
            # Cập nhật global variables
            with frame_lock:
                current_frame = processed_frame
                motion_detected = has_motion
        else:
            processed_frame = frame
            with frame_lock:
                current_frame = processed_frame
                motion_detected = False
        
        # Encode frame thành JPEG
        ret, buffer = cv2.imencode('.jpg', processed_frame, 
                                   [cv2.IMWRITE_JPEG_QUALITY, 85])
        if not ret:
            continue
        
        frame_bytes = buffer.tobytes()
        
        # Yield frame trong format multipart
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def index():
    """Trang chủ - hiển thị camera stream"""
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    """
    Endpoint để streaming video
    """
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


@app.route('/status')
def status():
    """
    API trả về trạng thái camera và motion detection
    """
    with frame_lock:
        return jsonify({
            'camera_active': camera.is_opened if camera else False,
            'motion_detected': motion_detected,
            'last_capture_time': last_capture_time
        })


@app.route('/captures')
def list_captures():
    """
    Trang hiển thị danh sách ảnh đã chụp
    """
    if not os.path.exists(config.CAPTURES_DIR):
        return render_template('captures.html', images=[])
    
    # Lấy danh sách file ảnh, sắp xếp theo thời gian (mới nhất trước)
    images = [f for f in os.listdir(config.CAPTURES_DIR) 
              if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    images.sort(reverse=True)
    
    return render_template('captures.html', images=images)


@app.route('/captures/<filename>')
def serve_capture(filename):
    """
    Phục vụ file ảnh đã chụp
    """
    return send_from_directory(config.CAPTURES_DIR, filename)


@app.route('/camera/start', methods=['POST'])
def start_camera():
    """
    API để bật camera
    """
    global camera, motion_detector
    
    with frame_lock:
        if camera is None:
            camera = Camera()
        
        if camera.is_opened:
            return jsonify({
                'success': True,
                'message': 'Camera is already running',
                'camera_active': True
            })
        
        if camera.start():
            if motion_detector is None:
                motion_detector = MotionDetector()
            return jsonify({
                'success': True,
                'message': 'Camera started successfully',
                'camera_active': True
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to start camera',
                'camera_active': False
            }), 500


@app.route('/camera/stop', methods=['POST'])
def stop_camera():
    """
    API để tắt camera
    """
    global camera
    
    with frame_lock:
        if camera is None or not camera.is_opened:
            return jsonify({
                'success': True,
                'message': 'Camera is already stopped',
                'camera_active': False
            })
        
        camera.release()
        return jsonify({
            'success': True,
            'message': 'Camera stopped successfully',
            'camera_active': False
        })


@app.route('/camera/toggle', methods=['POST'])
def toggle_camera():
    """
    API để bật/tắt camera
    """
    global camera
    
    with frame_lock:
        if camera is None or not camera.is_opened:
            # Bật camera
            return start_camera()
        else:
            # Tắt camera
            return stop_camera()


def init_camera():
    """Khởi tạo camera và motion detector"""
    global camera, motion_detector
    
    print("Starting camera...")
    camera = Camera()
    if camera.start():
        motion_detector = MotionDetector()
        print("Camera and motion detector ready!")
        return True
    else:
        print("Cannot start camera!")
        return False


def cleanup():
    """Dọn dẹp khi thoát ứng dụng"""
    global camera
    if camera:
        camera.release()


if __name__ == '__main__':
    # Khởi tạo camera
    if not init_camera():
        print("Error: Cannot start camera. Please check connection.")
        exit(1)
    
    try:
        print(f"\n{'='*50}")
        print("Camera IoT - Motion Detection")
        print(f"{'='*50}")
        print(f"Server running at: http://{config.HOST}:{config.PORT}")
        print(f"Or access from other device: http://<YOUR_IP>:{config.PORT}")
        print(f"{'='*50}\n")
        
        app.run(
            host=config.HOST,
            port=config.PORT,
            debug=config.DEBUG,
            threaded=True
        )
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        cleanup()


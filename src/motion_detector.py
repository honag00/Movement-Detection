"""
Module phát hiện chuyển động sử dụng OpenCV
"""
import cv2
import numpy as np
from . import config
from datetime import datetime
import os


class MotionDetector:
    """
    Lớp phát hiện chuyển động sử dụng Background Subtraction (MOG2)
    
    Sử dụng thuật toán MOG2 (Mixture of Gaussians) để phát hiện
    các đối tượng chuyển động trong video stream.
    """
    
    def __init__(self):
        """Khởi tạo motion detector"""
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(
            detectShadows=True,
            varThreshold=config.THRESHOLD_VALUE
        )
        self.min_area = config.MIN_AREA
        
        # Tạo thư mục lưu ảnh nếu chưa có
        if not os.path.exists(config.CAPTURES_DIR):
            os.makedirs(config.CAPTURES_DIR)
            print(f"Đã tạo thư mục {config.CAPTURES_DIR}")
    
    def detect(self, frame):
        """
        Phát hiện chuyển động trong frame
        :param frame: Frame từ camera (numpy array)
        :return: Tuple (has_motion, processed_frame, contours)
            - has_motion: Boolean, True nếu phát hiện chuyển động
            - processed_frame: Frame đã được vẽ contours và bounding boxes
            - contours: List các contours phát hiện được
        """
        # Áp dụng background subtractor
        fg_mask = self.bg_subtractor.apply(frame)
        
        # Làm mịn mask để loại bỏ nhiễu
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
        
        # Tìm contours
        contours, _ = cv2.findContours(
            fg_mask, 
            cv2.RETR_EXTERNAL, 
            cv2.CHAIN_APPROX_SIMPLE
        )
        
        # Lọc contours theo diện tích
        valid_contours = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > self.min_area:
                valid_contours.append(contour)
        
        has_motion = len(valid_contours) > 0
        
        # Vẽ contours lên frame nếu có chuyển động
        processed_frame = frame.copy()
        if has_motion:
            cv2.drawContours(processed_frame, valid_contours, -1, (0, 255, 0), 2)
            
            # Vẽ bounding box cho mỗi contour
            for contour in valid_contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(processed_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    processed_frame,
                    "MOTION",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )
        
        return has_motion, processed_frame, valid_contours
    
    def save_capture(self, frame, prefix="motion"):
        """
        Lưu ảnh khi phát hiện chuyển động
        :param frame: Frame cần lưu (numpy array)
        :param prefix: Tiền tố tên file
        :return: Đường dẫn file đã lưu
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"{prefix}_{timestamp}.jpg"
        filepath = os.path.join(config.CAPTURES_DIR, filename)
        
        cv2.imwrite(filepath, frame)
        return filepath


"""
Module quản lý camera và capture frames
"""
import cv2
from . import config


class Camera:
    """
    Lớp quản lý camera để capture video frames
    
    Attributes:
        camera_index (int): Index của camera
        cap (cv2.VideoCapture): OpenCV VideoCapture object
        is_opened (bool): Trạng thái camera đã mở hay chưa
    """
    
    def __init__(self, camera_index=None):
        """
        Khởi tạo camera
        :param camera_index: Index của camera (None để dùng config)
        """
        self.camera_index = camera_index if camera_index is not None else config.CAMERA_INDEX
        self.cap = None
        self.is_opened = False
        
    def start(self):
        """
        Bắt đầu capture từ camera
        :return: True nếu thành công, False nếu thất bại
        """
        try:
            self.cap = cv2.VideoCapture(self.camera_index)
            if not self.cap.isOpened():
                raise Exception(f"Không thể mở camera tại index {self.camera_index}")
            
            # Thiết lập kích thước frame
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.FRAME_WIDTH)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.FRAME_HEIGHT)
            self.cap.set(cv2.CAP_PROP_FPS, config.FPS)
            
            self.is_opened = True
            print(f"Camera started at index {self.camera_index}")
            return True
        except Exception as e:
            print(f"Error starting camera: {e}")
            self.is_opened = False
            return False
    
    def read(self):
        """
        Đọc frame từ camera
        :return: (success, frame) hoặc (False, None) nếu lỗi
        """
        if not self.is_opened or self.cap is None:
            return False, None
        
        ret, frame = self.cap.read()
        if not ret:
            return False, None
        
        return True, frame
    
    def release(self):
        """Giải phóng camera"""
        if self.cap is not None:
            self.cap.release()
            self.is_opened = False
            print("Camera released")
    
    def __enter__(self):
        """Context manager entry"""
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.release()

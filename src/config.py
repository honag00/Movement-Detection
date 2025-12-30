"""
Cấu hình cho Camera IoT - Phát hiện chuyển động
"""
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Camera settings
CAMERA_INDEX = 0  # 0 cho webcam mặc định, thay đổi nếu dùng camera khác
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FPS = 30

# Motion detection settings
MIN_AREA = 500  # Diện tích tối thiểu để coi là chuyển động (pixels)
THRESHOLD_VALUE = 25  # Ngưỡng phát hiện chuyển động
GAUSSIAN_BLUR = (21, 21)  # Kích thước blur để làm mịn
ACCUM_WEIGHT = 0.5  # Trọng số cho background accumulator

# File paths
CAPTURES_DIR = os.path.join(BASE_DIR, "captures")  # Thư mục lưu ảnh khi phát hiện chuyển động
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Flask settings
HOST = "0.0.0.0"  # Cho phép truy cập từ mọi IP
PORT = 5000
DEBUG = True

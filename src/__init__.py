"""
Camera IoT - Phát hiện chuyển động
Một dự án IoT sử dụng Computer Vision để giám sát và phát hiện chuyển động
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .camera import Camera
from .motion_detector import MotionDetector
from . import config

__all__ = ['Camera', 'MotionDetector', 'config']


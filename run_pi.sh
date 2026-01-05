#!/bin/bash
# Script chạy ứng dụng trên Raspberry Pi 3

echo "=========================================="
echo "Khởi động Camera IoT - Motion Detection"
echo "=========================================="
echo ""

# Kiểm tra virtual environment
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment chưa được tạo!"
    echo "Vui lòng chạy: ./setup_pi.sh"
    exit 1
fi

# Kích hoạt virtual environment
echo "🔧 Kích hoạt virtual environment..."
source .venv/bin/activate

# Kiểm tra Python packages
echo "🔍 Kiểm tra dependencies..."
python3 -c "import cv2, flask, numpy" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Thiếu dependencies. Đang cài đặt..."
    pip install -r requirements.txt
fi

# Lấy IP address của Raspberry Pi
echo ""
echo "🌐 Địa chỉ IP của Raspberry Pi:"
hostname -I | awk '{print $1}'
echo ""

# Chạy ứng dụng
echo "🚀 Đang khởi động ứng dụng..."
echo "Truy cập tại: http://$(hostname -I | awk '{print $1}'):5000"
echo "Hoặc từ máy khác: http://<IP_RASPBERRY_PI>:5000"
echo ""
echo "Nhấn Ctrl+C để dừng ứng dụng"
echo ""

python3 app.py


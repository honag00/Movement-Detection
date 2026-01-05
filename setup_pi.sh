#!/bin/bash
# Script cài đặt cho Raspberry Pi 3
# Chạy script này trên Raspberry Pi để cài đặt tất cả dependencies

echo "=========================================="
echo "Cài đặt Camera IoT - Motion Detection"
echo "Cho Raspberry Pi 3"
echo "=========================================="
echo ""

# Kiểm tra Python
echo "📦 Kiểm tra Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 chưa được cài đặt. Đang cài đặt..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip python3-venv
else
    echo "✅ Python3 đã được cài đặt: $(python3 --version)"
fi

# Kiểm tra pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 chưa được cài đặt. Đang cài đặt..."
    sudo apt-get install -y python3-pip
else
    echo "✅ pip3 đã được cài đặt"
fi

# Cài đặt các dependencies hệ thống cho OpenCV
echo ""
echo "📦 Cài đặt dependencies hệ thống cho OpenCV..."
sudo apt-get update
sudo apt-get install -y \
    libopencv-dev \
    python3-opencv \
    libatlas-base-dev \
    libjasper-dev \
    libqtgui4 \
    libqt4-test \
    python3-pyqt5 \
    libhdf5-dev \
    libhdf5-serial-dev \
    libharfbuzz0b \
    libwebp-dev \
    libtiff5-dev \
    libjxr-dev \
    libopenexr-dev \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev

# Tạo virtual environment
echo ""
echo "📦 Tạo virtual environment..."
if [ -d ".venv" ]; then
    echo "⚠️  Virtual environment đã tồn tại. Bỏ qua..."
else
    python3 -m venv .venv
    echo "✅ Đã tạo virtual environment"
fi

# Kích hoạt virtual environment và cài đặt packages
echo ""
echo "📦 Cài đặt Python packages..."
source .venv/bin/activate

# Nâng cấp pip
pip install --upgrade pip

# Cài đặt các packages từ requirements.txt
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✅ Đã cài đặt các packages từ requirements.txt"
else
    echo "⚠️  Không tìm thấy requirements.txt. Cài đặt thủ công..."
    pip install opencv-python flask numpy imutils
fi

# Tạo thư mục Pictures nếu chưa có (cho Linux)
echo ""
echo "📁 Tạo thư mục lưu ảnh..."
mkdir -p ~/Pictures/demo_camera
echo "✅ Đã tạo thư mục ~/Pictures/demo_camera"

# Kiểm tra camera
echo ""
echo "📷 Kiểm tra camera..."
if [ -e /dev/video0 ]; then
    echo "✅ Tìm thấy camera tại /dev/video0"
elif [ -e /dev/video1 ]; then
    echo "✅ Tìm thấy camera tại /dev/video1"
    echo "⚠️  Lưu ý: Có thể cần thay đổi CAMERA_INDEX trong src/config.py thành 1"
else
    echo "⚠️  Không tìm thấy camera. Đảm bảo camera đã được kết nối."
fi

echo ""
echo "=========================================="
echo "✅ Cài đặt hoàn tất!"
echo "=========================================="
echo ""
echo "Để chạy ứng dụng, sử dụng:"
echo "  ./run_pi.sh"
echo ""
echo "Hoặc chạy thủ công:"
echo "  source .venv/bin/activate"
echo "  python app.py"
echo ""


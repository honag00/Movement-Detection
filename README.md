# 📹 Camera IoT - Phát hiện chuyển động

Một dự án IoT sử dụng Computer Vision để giám sát và phát hiện chuyển động thời gian thực. Dự án kết hợp OpenCV, Python và Flask để tạo ra một hệ thống camera thông minh có thể phát hiện chuyển động và tự động lưu ảnh.

## ✨ Tính năng

- 🎥 **Streaming video thời gian thực** - Xem camera trực tiếp qua trình duyệt web
- 🔍 **Phát hiện chuyển động tự động** - Sử dụng thuật toán Background Subtraction (MOG2)
- 📸 **Tự động chụp ảnh** - Lưu ảnh khi phát hiện chuyển động
- 🌐 **Giao diện web hiện đại** - Responsive design, dễ sử dụng
- 📊 **Trạng thái real-time** - Hiển thị trạng thái camera và motion detection
- 🖼️ **Gallery ảnh** - Xem lại tất cả ảnh đã chụp

## 🛠️ Công nghệ sử dụng

- **Python 3.7+** - Ngôn ngữ lập trình chính
- **OpenCV** - Xử lý hình ảnh và phát hiện chuyển động
- **Flask** - Web framework cho streaming và API
- **NumPy** - Xử lý mảng và tính toán
- **HTML/CSS/JavaScript** - Giao diện người dùng

## 📋 Yêu cầu hệ thống

- Python 3.7 trở lên
- Camera (Webcam, USB Camera, hoặc Raspberry Pi Camera)
- Kết nối mạng (để truy cập từ thiết bị khác)

## 🚀 Cài đặt

### 1. Clone repository

```bash
git clone <repository-url>
cd camera-project
```

### 2. Cài đặt tự động (Khuyến nghị)

**Windows (PowerShell):**
```powershell
.\.dev\setup.ps1
```

**Windows (CMD):**
```cmd
.dev\setup.bat
```

### 3. Cài đặt thủ công

**Tạo virtual environment:**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

**Cài đặt dependencies:**
```bash
pip install -r requirements.txt
```

> **Lưu ý:** Nếu gặp lỗi "Import flask could not be resolved" trong IDE, đây là do packages chưa được cài đặt. Chạy script setup hoặc cài đặt thủ công như trên.

### 4. Khắc phục lỗi Import trong IDE

Nếu bạn thấy lỗi `Import "flask" could not be resolved` hoặc `Import "cv2" could not be resolved` trong IDE:

1. **Chọn đúng Python Interpreter:**
   - VS Code/Cursor: Nhấn `Ctrl+Shift+P` → `Python: Select Interpreter`
   - Chọn: `.venv\Scripts\python.exe`

2. **Reload IDE:**
   - Nhấn `Ctrl+Shift+P` → `Developer: Reload Window`

3. **Đảm bảo packages đã được cài:**
   ```bash
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

> **Lưu ý:** Lỗi này **KHÔNG phải lỗi code** - đây chỉ là cảnh báo của IDE vì chưa tìm thấy packages. Sau khi chọn đúng interpreter, lỗi sẽ biến mất.

## 💻 Sử dụng

### 1. Cấu hình camera

Mở file `src/config.py` và chỉnh sửa các thông số:

```python
CAMERA_INDEX = 0  # 0 cho webcam mặc định, 1, 2... cho camera khác
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
```

### 2. Chạy ứng dụng

**Cách 1: Sử dụng script (Khuyến nghị)**
```powershell
# PowerShell
.\.dev\run.ps1

# CMD
.dev\run.bat
```

**Cách 2: Chạy thủ công**
```bash
# Kích hoạt virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Chạy ứng dụng
python app.py
```

### 3. Truy cập web interface

- **Local**: http://localhost:5000
- **Từ thiết bị khác**: http://<IP_MAY_TINH>:5000

## ⚙️ Cấu hình

Các thông số có thể tùy chỉnh trong `src/config.py`:

### Camera Settings
- `CAMERA_INDEX`: Index của camera (0, 1, 2...)
- `FRAME_WIDTH`: Chiều rộng frame (pixels)
- `FRAME_HEIGHT`: Chiều cao frame (pixels)
- `FPS`: Frames per second

### Motion Detection Settings
- `MIN_AREA`: Diện tích tối thiểu để phát hiện chuyển động (pixels)
- `THRESHOLD_VALUE`: Ngưỡng phát hiện chuyển động
- `GAUSSIAN_BLUR`: Kích thước blur để làm mịn

### Server Settings
- `HOST`: Địa chỉ IP server (0.0.0.0 để truy cập từ mọi IP)
- `PORT`: Cổng server (mặc định: 5000)
- `DEBUG`: Chế độ debug (True/False)

## 📁 Cấu trúc dự án

```
camera-project/
├── app.py                 # Flask application chính
├── requirements.txt       # Python dependencies
├── README.md             # Tài liệu dự án
├── LICENSE               # Giấy phép
├── .gitignore           # Git ignore file
├── .dev/                # Development tools & scripts
│   ├── setup.ps1        # Setup script (PowerShell)
│   ├── setup.bat        # Setup script (CMD)
│   ├── run.ps1          # Run script (PowerShell)
│   └── run.bat          # Run script (CMD)
├── src/                 # Source code modules
│   ├── __init__.py
│   ├── camera.py        # Module quản lý camera
│   ├── motion_detector.py  # Module phát hiện chuyển động
│   └── config.py        # File cấu hình
└── templates/           # HTML templates
    ├── index.html       # Trang chủ với video stream
    └── captures.html    # Trang gallery ảnh
```

**Lưu ý:**
- Thư mục `captures/` sẽ được tự động tạo khi chạy ứng dụng
- Thư mục `.venv/` sẽ được tạo khi chạy setup script
- File `__pycache__/` sẽ được tự động tạo khi chạy Python (đã được ignore trong .gitignore)

## 🔧 API Endpoints

- `GET /` - Trang chủ với video stream
- `GET /video_feed` - Video stream endpoint
- `GET /status` - API trả về trạng thái camera và motion detection
- `POST /camera/toggle` - Bật/tắt camera
- `POST /camera/start` - Bật camera
- `POST /camera/stop` - Tắt camera
- `GET /captures` - Trang hiển thị danh sách ảnh đã chụp
- `GET /captures/<filename>` - Lấy file ảnh đã chụp

## 🎯 Ứng dụng

- **An ninh gia đình** - Giám sát nhà cửa khi vắng mặt
- **IoT Projects** - Tích hợp vào hệ thống IoT lớn hơn
- **Học tập** - Dự án thực hành Computer Vision và IoT
- **Portfolio** - Dự án demo kỹ năng lập trình

## 📝 Ghi chú

- Ảnh được tự động lưu vào thư mục `captures/` khi phát hiện chuyển động
- Có cooldown 2 giây giữa các lần chụp ảnh để tránh spam
- Hệ thống sử dụng Background Subtraction để phát hiện chuyển động, cần thời gian khởi động để học background

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng tạo issue hoặc pull request.

## 📄 License

Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 👤 Tác giả

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

⭐ Nếu dự án này hữu ích, hãy cho một star!


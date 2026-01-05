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

### 1. Clone repository hoặc copy code lên Raspberry Pi

**Nếu có Git trên Raspberry Pi:**
```bash
git clone <repository-url>
cd movement_detector
```

**Nếu không có Git, copy code từ máy Windows:**
```bash
# Trên máy Windows, sử dụng SCP hoặc SFTP để copy code
# Ví dụ với WinSCP, FileZilla, hoặc PowerShell:
scp -r C:\Users\USER\Desktop\movement_detector pi@<IP_RASPBERRY_PI>:~/movement_detector

# Sau đó SSH vào Raspberry Pi:
ssh pi@<IP_RASPBERRY_PI>
cd ~/movement_detector
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

**Raspberry Pi 3 (Linux):**
```bash
# Cấp quyền thực thi cho script
chmod +x setup_pi.sh

# Chạy script cài đặt
./setup_pi.sh
```

> **Lưu ý cho Raspberry Pi:** Script sẽ tự động cài đặt tất cả dependencies hệ thống cần thiết cho OpenCV, bao gồm các thư viện camera và xử lý hình ảnh.

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

**Windows:**
```powershell
# PowerShell
.\.dev\run.ps1

# CMD
.dev\run.bat
```

**Raspberry Pi 3:**
```bash
# Cấp quyền thực thi
chmod +x run_pi.sh

# Chạy ứng dụng
./run_pi.sh
```

**Cách 2: Chạy thủ công**
```bash
# Kích hoạt virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac/Raspberry Pi

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
  - **Windows**: Thường là 0 cho webcam mặc định
  - **Raspberry Pi**: 
    - 0 cho USB camera
    - Nếu dùng Raspberry Pi Camera Module, có thể cần sử dụng `picamera2` library (xem phần Raspberry Pi bên dưới)
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
movement_detector/
├── app.py                 # Flask application chính
├── requirements.txt       # Python dependencies
├── README.md             # Tài liệu dự án
├── LICENSE               # Giấy phép
├── setup_pi.sh           # Setup script cho Raspberry Pi
├── run_pi.sh             # Run script cho Raspberry Pi
├── .dev/                # Development tools & scripts (Windows)
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

## 🍓 Hướng dẫn cho Raspberry Pi 3

### Chuẩn bị

1. **Cài đặt Raspberry Pi OS** (Raspberry Pi OS Lite hoặc Desktop)
2. **Kết nối camera:**
   - USB Camera: Cắm vào cổng USB
   - Raspberry Pi Camera Module: Kết nối vào cổng CSI
3. **Kết nối mạng:** Đảm bảo Raspberry Pi đã kết nối WiFi hoặc Ethernet

### Các bước triển khai

1. **Copy code lên Raspberry Pi:**
   ```bash
   # Từ máy Windows, sử dụng SCP
   scp -r C:\Users\USER\Desktop\movement_detector pi@<IP_RASPBERRY_PI>:~/
   
   # Hoặc sử dụng USB drive, Git, hoặc các công cụ khác
   ```

2. **SSH vào Raspberry Pi:**
   ```bash
   ssh pi@<IP_RASPBERRY_PI>
   # Mật khẩu mặc định thường là "raspberry"
   ```

3. **Chạy script cài đặt:**
   ```bash
   cd ~/movement_detector
   chmod +x setup_pi.sh
   ./setup_pi.sh
   ```
   
   Script sẽ tự động:
   - Cài đặt Python3 và pip3 (nếu chưa có)
   - Cài đặt các dependencies hệ thống cho OpenCV
   - Tạo virtual environment
   - Cài đặt Python packages
   - Tạo thư mục lưu ảnh

4. **Cấu hình camera (nếu cần):**
   ```bash
   # Mở file config
   nano src/config.py
   
   # Thay đổi CAMERA_INDEX nếu camera không ở index 0
   # Kiểm tra camera có sẵn:
   ls -l /dev/video*
   ```

5. **Chạy ứng dụng:**
   ```bash
   chmod +x run_pi.sh
   ./run_pi.sh
   ```

6. **Truy cập từ máy khác:**
   - Từ trình duyệt: `http://<IP_RASPBERRY_PI>:5000`
   - Tìm IP của Raspberry Pi: `hostname -I`

### Chạy tự động khi khởi động (Tùy chọn)

Để ứng dụng tự động chạy khi Raspberry Pi khởi động:

1. **Tạo systemd service:**
   ```bash
   sudo nano /etc/systemd/system/motion-detector.service
   ```

2. **Thêm nội dung sau:**
   ```ini
   [Unit]
   Description=Motion Detector Camera Service
   After=network.target

   [Service]
   Type=simple
   User=pi
   WorkingDirectory=/home/pi/movement_detector
   ExecStart=/home/pi/movement_detector/.venv/bin/python3 /home/pi/movement_detector/app.py
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

3. **Kích hoạt service:**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable motion-detector.service
   sudo systemctl start motion-detector.service
   ```

4. **Kiểm tra trạng thái:**
   ```bash
   sudo systemctl status motion-detector.service
   ```

### Lưu ý cho Raspberry Pi

- **Hiệu năng:** Raspberry Pi 3 có thể xử lý tốt với độ phân giải 640x480. Nếu muốn tăng độ phân giải, có thể cần giảm FPS.
- **Nhiệt độ:** Đảm bảo Raspberry Pi có tản nhiệt tốt khi chạy liên tục.
- **Nguồn điện:** Sử dụng nguồn 5V 2.5A trở lên để đảm bảo ổn định.
- **Camera Module:** Nếu dùng Raspberry Pi Camera Module (không phải USB), có thể cần điều chỉnh code để sử dụng `picamera2` thay vì OpenCV VideoCapture.

## 📝 Ghi chú

- Ảnh được tự động lưu vào thư mục `~/Pictures/demo_camera/` (Linux/Raspberry Pi) hoặc `Pictures/demo_camera/` (Windows) khi phát hiện chuyển động
- Có cooldown 2 giây giữa các lần chụp ảnh để tránh spam
- Hệ thống sử dụng Background Subtraction để phát hiện chuyển động, cần thời gian khởi động để học background

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng tạo issue hoặc pull request.

## 📄 License

Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 👤 Tác giả

**Your Name**

- GitHub: [@honag00](https://github.com/honag00)
- Email: djhoangnguyen2003@gmail.com

---

⭐ Nếu dự án này hữu ích, hãy cho một star!


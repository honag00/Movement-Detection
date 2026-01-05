# 🍓 Hướng dẫn nhanh - Triển khai lên Raspberry Pi 3

## Bước 1: Copy code lên Raspberry Pi

### Cách 1: Sử dụng SCP (từ máy Windows)

```powershell
# Trong PowerShell trên Windows
scp -r C:\Users\USER\Desktop\movement_detector pi@<IP_RASPBERRY_PI>:~/
```

Thay `<IP_RASPBERRY_PI>` bằng địa chỉ IP của Raspberry Pi (ví dụ: `192.168.1.100`)

### Cách 2: Sử dụng WinSCP hoặc FileZilla

1. Tải WinSCP hoặc FileZilla
2. Kết nối đến Raspberry Pi với thông tin:
   - Host: `<IP_RASPBERRY_PI>`
   - Username: `pi`
   - Password: `raspberry` (hoặc mật khẩu bạn đã đặt)
3. Copy toàn bộ thư mục `movement_detector` lên thư mục home của Pi (`/home/pi/`)

### Cách 3: Sử dụng USB Drive

1. Copy thư mục `movement_detector` vào USB drive
2. Cắm USB vào Raspberry Pi
3. Copy từ USB vào thư mục home:
   ```bash
   cp -r /media/pi/<USB_NAME>/movement_detector ~/
   ```

## Bước 2: SSH vào Raspberry Pi

```bash
ssh pi@<IP_RASPBERRY_PI>
```

## Bước 3: Chạy script cài đặt

```bash
cd ~/movement_detector
chmod +x setup_pi.sh
./setup_pi.sh
```

Script sẽ mất khoảng 10-15 phút để cài đặt tất cả dependencies.

## Bước 4: Kiểm tra camera

```bash
# Kiểm tra camera USB
ls -l /dev/video*

# Nếu thấy /dev/video0 hoặc /dev/video1, camera đã được nhận diện
```

Nếu camera ở `/dev/video1` thay vì `/dev/video0`, cần chỉnh sửa `src/config.py`:
```bash
nano src/config.py
# Thay đổi CAMERA_INDEX = 0 thành CAMERA_INDEX = 1
```

## Bước 5: Chạy ứng dụng

```bash
chmod +x run_pi.sh
./run_pi.sh
```

## Bước 6: Truy cập từ máy khác

1. Lấy IP của Raspberry Pi:
   ```bash
   hostname -I
   ```

2. Từ trình duyệt trên máy khác, truy cập:
   ```
   http://<IP_RASPBERRY_PI>:5000
   ```

## Chạy tự động khi khởi động (Tùy chọn)

Nếu muốn ứng dụng tự động chạy khi Raspberry Pi khởi động:

```bash
# Tạo file service
sudo nano /etc/systemd/system/motion-detector.service
```

Thêm nội dung sau (thay đổi đường dẫn nếu cần):
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

Lưu file (Ctrl+O, Enter, Ctrl+X), sau đó:

```bash
# Kích hoạt service
sudo systemctl daemon-reload
sudo systemctl enable motion-detector.service
sudo systemctl start motion-detector.service

# Kiểm tra trạng thái
sudo systemctl status motion-detector.service
```

## Xử lý lỗi thường gặp

### Lỗi: "Cannot start camera"
- Kiểm tra camera đã được kết nối: `ls -l /dev/video*`
- Kiểm tra quyền truy cập camera: `groups pi` (phải có `video` group)
- Nếu thiếu quyền: `sudo usermod -a -G video pi` và đăng nhập lại

### Lỗi: "Import cv2 could not be resolved"
- Đảm bảo đã chạy `setup_pi.sh` hoàn tất
- Kích hoạt virtual environment: `source .venv/bin/activate`
- Cài đặt lại: `pip install opencv-python`

### Lỗi: "Permission denied" khi chạy script
- Cấp quyền thực thi: `chmod +x setup_pi.sh run_pi.sh`

### Ứng dụng chạy chậm
- Giảm độ phân giải trong `src/config.py`: `FRAME_WIDTH = 320, FRAME_HEIGHT = 240`
- Giảm FPS: `FPS = 15`

## Liên hệ

Nếu gặp vấn đề, vui lòng tạo issue trên GitHub hoặc liên hệ tác giả.


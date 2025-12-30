@echo off
echo ========================================
echo Camera IoT - Setup Script
echo ========================================
echo.

REM Kiểm tra Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python chua duoc cai dat hoac chua co trong PATH!
    echo.
    echo Vui long:
    echo 1. Cai dat Python tu https://www.python.org/downloads/
    echo 2. Khi cai dat, nho chon "Add Python to PATH"
    echo 3. Chay lai script nay
    pause
    exit /b 1
)

echo [OK] Python da duoc tim thay
python --version
echo.

REM Tạo virtual environment
echo [1/3] Dang tao virtual environment...
if exist .venv (
    echo Virtual environment da ton tai, bo qua...
) else (
    python -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Khong the tao virtual environment!
        pause
        exit /b 1
    )
    echo [OK] Virtual environment da duoc tao
)
echo.

REM Kích hoạt virtual environment và cài packages
echo [2/3] Dang kich hoat virtual environment...
call .venv\Scripts\activate.bat
echo.

echo [3/3] Dang cai dat packages...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Khong the cai dat packages!
    pause
    exit /b 1
)
echo.

echo ========================================
echo [SUCCESS] Cai dat thanh cong!
echo ========================================
echo.
echo De chay ung dung:
echo   1. Kich hoat virtual environment: .venv\Scripts\activate.bat
echo   2. Chay: python app.py
echo.
pause


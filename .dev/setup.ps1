# Camera IoT - Setup Script (PowerShell)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Camera IoT - Setup Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Kiểm tra Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python da duoc tim thay: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python chua duoc cai dat hoac chua co trong PATH!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Vui long:" -ForegroundColor Yellow
    Write-Host "1. Cai dat Python tu https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "2. Khi cai dat, nho chon 'Add Python to PATH'" -ForegroundColor Yellow
    Write-Host "3. Chay lai script nay" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Tạo virtual environment
Write-Host "[1/3] Dang tao virtual environment..." -ForegroundColor Yellow
if (Test-Path .venv) {
    Write-Host "Virtual environment da ton tai, bo qua..." -ForegroundColor Gray
} else {
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Khong the tao virtual environment!" -ForegroundColor Red
        exit 1
    }
    Write-Host "[OK] Virtual environment da duoc tao" -ForegroundColor Green
}
Write-Host ""

# Kích hoạt virtual environment
Write-Host "[2/3] Dang kich hoat virtual environment..." -ForegroundColor Yellow
& .venv\Scripts\Activate.ps1
Write-Host ""

# Cài đặt packages
Write-Host "[3/3] Dang cai dat packages..." -ForegroundColor Yellow
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Khong the cai dat packages!" -ForegroundColor Red
    exit 1
}
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "[SUCCESS] Cai dat thanh cong!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "De chay ung dung:" -ForegroundColor Yellow
Write-Host "  1. Kich hoat virtual environment: .venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "  2. Chay: python app.py" -ForegroundColor White
Write-Host ""


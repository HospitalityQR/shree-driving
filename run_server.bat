@echo off
title LOTUS HUT — SWIGGY PAYMENT & ORDER SERVER
echo =========================================================================
echo    LOTUS HUT — THE DRIVE IN CAFE
echo    Swiggy-Inspired Secure Payment & Order Management Server
echo =========================================================================
echo.

cd /d "%~dp0"

echo [1/3] Checking Python installation...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [!] Python is not found in your PATH. Opening static pages directly...
    start "" "payment.html"
    start "" "index.html"
    pause
    exit /b
)

echo [2/3] Checking / Installing dependencies...
python -m pip install -r requirements.txt --quiet

echo [3/3] Starting Payment Backend Server on http://127.0.0.1:5000 ...
echo.
echo  • Swiggy Checkout:  http://127.0.0.1:5000/payment.html
echo  • Customer Menu:    http://127.0.0.1:5000/
echo  • Staff Terminal:   http://127.0.0.1:5000/staff.html
echo.
echo Opening Swiggy Payment Page in your browser...
start http://127.0.0.1:5000/payment.html

python app.py
pause

@echo off
echo =========================================================================
echo    LOTUS HUT — THE DRIVE IN CAFE (DIGITAL MENU & PAYMENT SYSTEM)
echo =========================================================================
echo Opening Customer Menu, Swiggy Payment Page & Staff Dashboard in your browser...
start "" "payment.html"
start "" "index.html"
start "" "staff.html"
echo.
echo Customer Menu:    index.html
echo Swiggy Payment:   payment.html
echo Staff Portal:     staff.html
echo.
echo For backend API server with full payment verification:
echo Double-click 'run_server.bat' to start the local Flask server on http://127.0.0.1:5000
echo.
echo Press any key to exit this window...
pause >nul

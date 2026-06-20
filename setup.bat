@echo off
echo ========================================
echo  Multilingual Learning Chatbot Setup
echo ========================================
echo.

echo [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)
echo Python found!
echo.

echo [2/4] Checking Node.js installation...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed!
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)
echo Node.js found!
echo.

echo [3/4] Setting up Backend...
cd backend
echo Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install Python dependencies
    pause
    exit /b 1
)
echo Backend setup complete!
cd ..
echo.

echo [4/4] Setting up Frontend...
cd frontend
echo Installing Node dependencies (this may take a few minutes)...
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install Node dependencies
    pause
    exit /b 1
)
echo Frontend setup complete!
cd ..
echo.

echo ========================================
echo  Setup Complete! 
echo ========================================
echo.
echo To start the application:
echo.
echo 1. Open a terminal and run:
echo    cd backend
echo    python main.py
echo.
echo 2. Open another terminal and run:
echo    cd frontend
echo    npm run dev
echo.
echo 3. Open browser at http://localhost:5173
echo.
echo ========================================
pause

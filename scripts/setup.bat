@echo off
REM Dental Clinic System - Setup Script for Windows

echo 🦷 Dental Clinic System Setup
echo ==============================

REM Check Python
echo 📋 Checking Python installation...
python --version
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.10+
    exit /b 1
)

REM Create virtual environment
echo 🔧 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo 📦 Installing requirements...
pip install -r dental_clinic_system\requirements.txt

REM Setup environment file
echo ⚙️  Setting up environment...
if not exist .env (
    copy .env.example .env
    echo ✓ Created .env file. Please update it with your settings.
)

REM Run migrations
echo 🗄️  Running database migrations...
cd dental_clinic_system
python manage.py migrate

REM Collect static files
echo 📁 Collecting static files...
python manage.py collectstatic --noinput

echo.
echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Update .env file with your settings
echo 2. Create superuser: python manage.py createsuperuser
echo 3. Run server: python manage.py runserver
echo.
echo Access the application at: http://127.0.0.1:8000

pause

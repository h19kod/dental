# 🚀 Installation Guide | دليل التثبيت

Complete installation guide for Dental Clinic Management System.

---

## 📋 Table of Contents
- [Requirements](#requirements)
- [Quick Installation](#quick-installation)
- [Detailed Installation](#detailed-installation)
- [Database Setup](#database-setup)
- [Environment Variables](#environment-variables)
- [Production Deployment](#production-deployment)
- [Troubleshooting](#troubleshooting)

---

## 📋 Requirements

### System Requirements
- **Operating System:** Windows 10/11, Linux, or macOS
- **Python:** 3.10 or higher
- **Memory:** 4GB RAM minimum (8GB recommended)
- **Disk Space:** 500MB minimum

### Required Software
- Python 3.10+
- pip (Python package manager)
- Git (optional, for cloning)

### Check Python Version
```bash
python --version
# or
python3 --version
```

---

## ⚡ Quick Installation (5 minutes)

### Step 1: Clone or Download Project
```bash
git clone https://github.com/yourusername/dental_clinic_system.git
cd dental_CAS
```

Or download and extract the ZIP file.

### Step 2: Run Setup Script
```bash
# Windows
python setup_windows.py

# Linux/Mac
make setup
```

### Step 3: Start the Server
```bash
cd dental_clinic_system
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## 📖 Detailed Installation

### Step 1: Create Virtual Environment

**Windows:**
```bash
cd "e:\New folder (3)\project\dental_CAS"
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
cd dental_CAS
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Verify Installation:**
```bash
pip list
```

You should see:
- Django 5.0.2
- djangorestframework 3.14.0
- drf-spectacular 0.27.1

### Step 3: Environment Configuration

1. **Copy environment template:**
```bash
cp .env.example .env
```

2. **Edit .env file:**
```env
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-change-in-production
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3

# Email (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Static & Media
MEDIA_URL=/media/
STATIC_URL=/static/
```

**Generate Secret Key:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 4: Database Setup

```bash
cd dental_clinic_system

# Run migrations
python manage.py migrate

# Verify database created
python manage.py dbshell
```

### Step 5: Create Admin User
```bash
python manage.py createsuperuser

# Enter:
# Username: admin
# Email: admin@dental.com
# Password: admin123
```

### Step 6: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Step 7: Create Sample Data (Optional)
```bash
python manage.py create_sample_data
```

---

## 🗄️ Database Setup

### SQLite (Default - Development)
```python
# Already configured in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### PostgreSQL (Production)

**1. Install PostgreSQL:**
```bash
# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib

# Windows
# Download from https://www.postgresql.org/download/windows/
```

**2. Create Database:**
```sql
CREATE DATABASE dental_clinic;
CREATE USER dental_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE dental_clinic TO dental_user;
```

**3. Update .env:**
```env
DATABASE_URL=postgres://dental_user:your_password@localhost:5432/dental_clinic
```

**4. Install psycopg2:**
```bash
pip install psycopg2-binary
```

**5. Run Migrations:**
```bash
python manage.py migrate
```

### MySQL (Alternative)

**1. Install MySQL:**
```bash
# Ubuntu
sudo apt-get install mysql-server

# Windows
# Download from https://dev.mysql.com/downloads/installer/
```

**2. Create Database:**
```sql
CREATE DATABASE dental_clinic CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'dental_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON dental_clinic.* TO 'dental_user'@'localhost';
```

**3. Install mysqlclient:**
```bash
pip install mysqlclient
```

**4. Update settings.py:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dental_clinic',
        'USER': 'dental_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
```

---

## 🔧 Environment Variables

### Complete .env Configuration

```env
# ============================================
# Django Core Settings
# ============================================
DEBUG=True
SECRET_KEY=your-super-secret-key-min-50-chars-long-for-security
ALLOWED_HOSTS=localhost,127.0.0.1,*.yourdomain.com

# ============================================
# Database Configuration
# ============================================
# SQLite (Development)
DATABASE_URL=sqlite:///db.sqlite3

# PostgreSQL (Production)
# DATABASE_URL=postgres://user:pass@localhost:5432/dbname

# MySQL (Production)
# DATABASE_URL=mysql://user:pass@localhost:3306/dbname

# ============================================
# Email Configuration (Optional)
# ============================================
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
DEFAULT_FROM_EMAIL=noreply@dentalclinic.com

# ============================================
# Static & Media Files
# ============================================
STATIC_URL=/static/
STATIC_ROOT=/var/www/dental/static
MEDIA_URL=/media/
MEDIA_ROOT=/var/www/dental/media

# ============================================
# Security Settings (Production)
# ============================================
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
SECURE_BROWSER_XSS_FILTER=True
SECURE_CONTENT_TYPE_NOSNIFF=True
X_FRAME_OPTIONS=DENY

# ============================================
# CORS Settings
# ============================================
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
CORS_ALLOW_ALL_ORIGINS=False

# ============================================
# Cache Settings (Optional - Redis)
# ============================================
# REDIS_URL=redis://localhost:6379/1
# CACHE_TIMEOUT=300

# ============================================
# Logging Level
# ============================================
LOG_LEVEL=INFO
```

---

## 🚀 Production Deployment

### Using Gunicorn + Nginx

**1. Install Gunicorn:**
```bash
pip install gunicorn
```

**2. Create Gunicorn Service:**

`/etc/systemd/system/dental.service`
```ini
[Unit]
Description=Dental Clinic Gunicorn daemon
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/dental/dental_clinic_system
ExecStart=/var/www/dental/venv/bin/gunicorn \
    --access-logfile - \
    --workers 3 \
    --bind unix:/var/www/dental/dental.sock \
    config.wsgi:application

[Install]
WantedBy=multi-user.target
```

**3. Nginx Configuration:**

`/etc/nginx/sites-available/dental`
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/dental/dental_clinic_system;
    }
    
    location /media/ {
        root /var/www/dental/dental_clinic_system;
    }
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/dental/dental.sock;
    }
}
```

**4. Enable Configuration:**
```bash
sudo ln -s /etc/nginx/sites-available/dental /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl start dental
sudo systemctl enable dental
```

### Using Docker

**1. Create Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN cd dental_clinic_system && python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dental_clinic_system.config.wsgi:application"]
```

**2. Create docker-compose.yml:**
```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: dental_clinic
      POSTGRES_USER: dental_user
      POSTGRES_PASSWORD: your_password

  web:
    build: .
    command: gunicorn dental_clinic_system.config.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - DATABASE_URL=postgres://dental_user:your_password@db:5432/dental_clinic
    depends_on:
      - db

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

**3. Run Docker:**
```bash
docker-compose up -d --build
docker-compose exec web python dental_clinic_system/manage.py migrate
docker-compose exec web python dental_clinic_system/manage.py createsuperuser
```

---

## ❗ Troubleshooting

### Common Issues

#### 1. "No module named 'django'"
```bash
# Solution: Activate virtual environment
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```

#### 2. "Secret Key Not Set"
```bash
# Solution: Create .env file
cp .env.example .env
# Edit .env and set SECRET_KEY
```

#### 3. "Permission Denied" (Linux/Mac)
```bash
# Solution: Fix permissions
chmod -R 755 dental_clinic_system
chmod 644 dental_clinic_system/db.sqlite3
```

#### 4. "Port 8000 Already in Use"
```bash
# Solution: Use different port
python manage.py runserver 8080
```

#### 5. "Static Files Not Loading"
```bash
# Solution: Collect static files
python manage.py collectstatic --clear --noinput
```

#### 6. "Migration Issues"
```bash
# Solution: Reset migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
python manage.py makemigrations
python manage.py migrate
```

### Getting Help

1. Check logs: `python manage.py runserver --verbosity 2`
2. Django admin: http://127.0.0.1:8000/admin/
3. API docs: http://127.0.0.1:8000/api/docs/
4. Check GitHub Issues or contact support

---

## ✅ Post-Installation Checklist

- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] .env file configured
- [ ] Database migrated
- [ ] Superuser created
- [ ] Static files collected
- [ ] Server running
- [ ] Login page accessible
- [ ] API docs accessible
- [ ] Sample data created (optional)

---

**🎉 Installation Complete!** Start using the system at http://127.0.0.1:8000/

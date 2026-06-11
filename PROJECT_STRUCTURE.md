# 📁 Project Structure | هيكل المشروع

Complete project structure and organization guide.

---

## 🗂️ Root Directory Structure

```
dental_CAS/                          # Project Root
│
├── 📄 README.md                      # Project overview and quick start
├── 📄 INSTALLATION.md                # Detailed installation guide
├── 📄 API_DOCUMENTATION.md           # REST API documentation
├── 📄 CONTRIBUTING.md                # Contribution guidelines
├── 📄 CHANGELOG.md                   # Version history and changes
├── 📄 PROJECT_STRUCTURE.md           # This file - project organization
├── 📄 LICENSE                        # MIT License
│
├── ⚙️  Configuration Files
│   ├── .env.example                  # Environment variables template
│   ├── .gitignore                    # Git ignore rules
│   ├── Makefile                      # Quick command shortcuts
│   ├── setup.py                      # Python package setup
│   └── docker-compose.yml            # Docker orchestration
│
├── 🔧 Scripts
│   ├── scripts/
│   │   ├── setup.sh                  # Linux/Mac setup script
│   │   ├── setup.bat                 # Windows setup script
│   │   └── backup.sh                 # Database backup script
│   │
└── 🏗️ dental_clinic_system/          # Main Django Project
    │
    ├── 🚀 Project Configuration
    │   ├── config/                   # Django settings
    │   │   ├── __init__.py
    │   │   ├── settings.py           # Main settings
    │   │   ├── urls.py               # URL routing
    │   │   ├── wsgi.py               # WSGI config
    │   │   └── asgi.py               # ASGI config
    │   │
    ├── 🎯 Django Apps
    │   │
    │   ├── accounts/                 # User Management App
    │   │   ├── __init__.py
    │   │   ├── admin.py              # Admin configurations
    │   │   ├── apps.py               # App configuration
    │   │   ├── models.py             # User model
    │   │   ├── serializers.py        # API serializers
    │   │   ├── views.py              # Views
    │   │   ├── tests.py              # Unit tests
    │   │   └── management/           # Custom commands
    │   │       ├── __init__.py
    │   │       └── commands/
    │   │           ├── __init__.py
    │   │           ├── create_sample_data.py
    │   │           └── reset_password.py
    │   │
    │   ├── patients/                 # Patient Management App
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py             # Patient model
    │   │   ├── serializers.py          # API serializers
    │   │   ├── views.py                # API views
    │   │   ├── urls.py                 # App URLs
    │   │   └── tests.py                # Tests
    │   │
    │   ├── doctors/                  # Doctor Management App
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py             # Doctor model
    │   │   ├── serializers.py
    │   │   ├── views.py
    │   │   ├── urls.py
    │   │   └── tests.py
    │   │
    │   └── appointments/             # Appointment Management App
    │       ├── __init__.py
    │       ├── admin.py
    │       ├── apps.py
    │       ├── models.py             # Appointment model
    │       ├── serializers.py
    │       ├── views.py
    │       ├── urls.py
    │       └── tests.py
    │
    ├── 🎨 Frontend Assets
    │   ├── static/                   # Static files
    │   │   ├── css/
    │   │   │   └── main.css          # Main stylesheet (Dark Mode)
    │   │   ├── js/
    │   │   │   └── main.js           # Main JavaScript
    │   │   └── images/               # Static images
    │   │
    │   └── media/                    # User-uploaded files
    │
    ├── 📝 Templates
    │   └── templates/
    │       ├── base/                 # Base templates
    │       │   ├── base.html         # Base layout
    │       │   └── sidebar.html      # Sidebar navigation
    │       ├── accounts/             # Account templates
    │       │   └── login.html        # Login page
    │       └── index.html            # Dashboard
    │
    ├── 🛠️ Utilities
    │   └── utils/                    # Shared utilities
    │       ├── __init__.py
    │       ├── middleware.py         # Custom middleware
    │       ├── validators.py         # Field validators
    │       ├── pagination.py         # API pagination
    │       └── helpers.py            # Helper functions
    │
    ├── 🐳 Deployment
    │   ├── Dockerfile                # Docker configuration
    │   ├── requirements.txt          # Python dependencies
    │   ├── .gitignore               # Project gitignore
    │   └── docs.md                  # Technical documentation
    │
    ├── 🗄️ Database
    │   └── db.sqlite3               # SQLite database (dev only)
    │
    └── 🔨 manage.py                 # Django management script
```

---

## 📋 File Naming Conventions

### Python Files
- `snake_case.py` for all Python files
- Tests: `test_<module>.py` or `tests.py`
- Migrations: Django auto-generated

### Static Files
- CSS: `main.css`, `components.css`
- JavaScript: `main.js`, `dashboard.js`
- Images: descriptive names with hyphens: `user-avatar.png`

### Templates
- Lowercase with hyphens: `login.html`, `user-profile.html`
- Base templates prefixed with `base-`

---

## 🔧 Development Workflow

### 1. Setup Environment
```bash
# Using script
./scripts/setup.sh          # Linux/Mac
scripts\setup.bat           # Windows

# Or manual
make setup
```

### 2. Run Development Server
```bash
make run
# or
cd dental_clinic_system
python manage.py runserver
```

### 3. Run Tests
```bash
make test
# or
python manage.py test
```

### 4. Create Backup
```bash
./scripts/backup.sh
```

---

## 📦 Key Dependencies

### Backend
- Django 5.0.2
- Django REST Framework 3.14.0
- drf-spectacular 0.27.1 (API docs)
- django-cors-headers 4.3.1
- Pillow 10.2.0 (Image handling)
- python-dotenv 1.0.1
- whitenoise 6.6.0 (Static files)
- gunicorn 21.2.0 (WSGI server)

### Frontend
- Bootstrap 5.3.0 (RTL)
- Bootstrap Icons 1.10.5
- Vanilla JavaScript (ES6+)

---

## 🔐 Security Considerations

### Environment Variables (.env)
```
DEBUG=False                    # Never True in production
SECRET_KEY=your-secret-key     # Generate strong key
ALLOWED_HOSTS=yourdomain.com   # Restrict domains
DATABASE_URL=postgres://...    # Use PostgreSQL in production
```

### Excluded from Git (.gitignore)
- `.env` - Environment secrets
- `db.sqlite3` - Database
- `media/` - User uploads
- `__pycache__/` - Python cache
- `venv/` - Virtual environment

---

## 🚀 Deployment Options

### 1. Local Development
```bash
python manage.py runserver
```

### 2. Docker
```bash
docker-compose up -d
```

### 3. Production Server
```bash
# Using Gunicorn
gunicorn config.wsgi:application
```

---

## 📚 Documentation Files

| File | Purpose | Language |
|------|---------|----------|
| README.md | Quick start & overview | Arabic/English |
| INSTALLATION.md | Setup guide | Arabic/English |
| API_DOCUMENTATION.md | API reference | English/Arabic |
| CONTRIBUTING.md | Contribution guide | English |
| CHANGELOG.md | Version history | Arabic |
| PROJECT_STRUCTURE.md | Organization guide | Arabic/English |
| docs.md | Technical docs | Arabic |

---

## ✅ Organization Checklist

- [x] Clear directory structure
- [x] Separation of concerns (apps)
- [x] Static files organization
- [x] Template inheritance
- [x] Utility modules
- [x] Configuration management
- [x] Documentation
- [x] Testing structure
- [x] Deployment configs
- [x] Scripts automation
- [x] Git ignore rules
- [x] License & contribution guidelines

---

**✨ Project fully organized and ready for development/deployment!**

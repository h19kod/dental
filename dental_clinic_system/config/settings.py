import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-pro-clinic-key-change-in-production')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # مكتبات إضافية
    'rest_framework',
    'corsheaders', 
    'drf_spectacular', # مكتبة التوثيق التفاعلي [cite: 2026-01-25]
    
    # تطبيقات المشروع
    'accounts',
    'patients',
    'doctors',
    'appointments',
]

AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Custom middleware
    'utils.middleware.SecurityHeadersMiddleware',
    'utils.middleware.RequestLoggingMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# إعدادات تسجيل الدخول [cite: 2026-01-25]
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

# الإعدادات الإقليمية [cite: 2026-01-25]
LANGUAGE_CODE = 'ar-sa'
TIME_ZONE = 'Asia/Baghdad'
USE_I18N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (User uploaded files)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# WhiteNoise for serving static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# إعدادات REST Framework والتوثيق التفاعلي [cite: 2026-01-25]
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'DENTAL PRO API Docs',
    'DESCRIPTION': 'التوثيق التفاعلي لروابط نظام عيادة الأسنان',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

CORS_ALLOW_ALL_ORIGINS = True
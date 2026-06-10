# 🦷 نظام إدارة عيادة الأسنان الذكي | DENTAL PRO System

![Django](https://img.shields.io/badge/Framework-Django-092e20?style=for-the-badge&logo=django)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap_5-7952b3?style=for-the-badge&logo=bootstrap)
![REST API](https://img.shields.io/badge/API-Swagger_Docs-green?style=for-the-badge&logo=swagger)

نظام متكامل لإدارة العيادات الطبية، مصمم لتوفير تجربة مستخدم سريعة وآمنة. يجمع المشروع بين قوة **Django** في الباكيند وأناقة **Bootstrap 5** في الواجهات، مع توفير توثيق كامل للـ APIs.

---

## 🌟 الميزات الرئيسية (Core Features)

### 1. لوحة تحكم عصرية (Professional Dashboard)
* واجهة مستخدم تعتمد على **الوضع الليلي (Dark Mode)** لراحة العين.
* عرض ملخص يومي لإجمالي المواعيد والعمليات.
* تصميم متجاوب (Responsive) يعمل على الحواسب والأجهزة اللوحية والموبايل.

### 2. نظام أمان متقدم (Authentication & Security)
* نظام تسجيل دخول وخروج محمي بالكامل.
* حماية الصفحات الحساسة (Middleware) لضمان عدم دخول غير المخولين.
* إدارة صلاحيات المستخدمين (أدمن، أطباء، موظف استقبال، مرضى).

### 3. البحث اللحظي (Live AJAX Search)
* ميزة البحث السريع عن المرضى والمواعيد باستخدام **JavaScript Fetch API**.
* تصفية النتائج فورياً دون الحاجة لإعادة تحميل الصفحة.

### 4. توثيق API تفاعلي (Swagger & OpenAPI)
* توفير صفحة Swagger UI لعرض واختبار الروابط برمجياً.
* سهولة الربط مع تطبيقات الموبايل مستقبلاً عبر الـ Endpoints الجاهزة.

---

## 🏗 بنية المشروع (Project Structure)

```
dental_CAS/
├── dental_clinic_system/          # المشروع الرئيسي
│   ├── config/                    # إعدادات Django
│   │   ├── settings.py           # الإعدادات الرئيسية
│   │   ├── urls.py               # روابط URL
│   │   ├── wsgi.py               # WSGI config
│   │   └── asgi.py               # ASGI config
│   │
│   ├── accounts/                  # تطبيق إدارة المستخدمين
│   │   ├── models.py             # نموذج المستخدم المخصص
│   │   ├── admin.py              # إعدادات الأدمن
│   │   ├── views.py              # الواجهات
│   │   └── urls.py               # روابط التطبيق
│   │
│   ├── patients/                  # تطبيق إدارة المرضى
│   │   ├── models.py             # نموذج المريض
│   │   ├── serializers.py        # محولات API
│   │   ├── views.py              # واجهات API
│   │   └── urls.py               # روابط API
│   │
│   ├── doctors/                   # تطبيق إدارة الأطباء
│   │   ├── models.py             # نموذج الطبيب
│   │   ├── serializers.py        # محولات API
│   │   ├── views.py              # واجهات API
│   │   └── urls.py               # روابط API
│   │
│   ├── appointments/              # تطبيق إدارة المواعيد
│   │   ├── models.py             # نموذج الموعد
│   │   ├── serializers.py        # محولات API
│   │   ├── views.py              # واجهات API
│   │   ├── urls.py               # روابط API
│   │   └── admin.py              # إعدادات الأدمن
│   │
│   ├── templates/                 # قوالب HTML
│   │   ├── base/                 # قوالب أساسية
│   │   │   ├── base.html         # القالب الرئيسي
│   │   │   └── sidebar.html      # القائمة الجانبية
│   │   ├── accounts/             # قوالب المستخدمين
│   │   │   └── login.html        # صفحة تسجيل الدخول
│   │   ├── appointments/         # قوالب المواعيد
│   │   ├── patients/             # قوالب المرضى
│   │   ├── doctors/              # قوالب الأطباء
│   │   └── index.html            # لوحة التحكم الرئيسية
│   │
│   ├── static/                    # الملفات الثابتة
│   │   ├── css/                  # ملفات CSS
│   │   │   └── main.css          # ملف الأنماط الرئيسي
│   │   ├── js/                   # ملفات JavaScript
│   │   │   └── main.js           # ملف JavaScript الرئيسي
│   │   └── images/               # الصور
│   │
│   ├── media/                     # ملفات المستخدمين المرفوعة
│   ├── utils/                     # أدوات مساعدة
│   │   └── helpers.py            # دوال مساعدة
│   ├── docs.md                    # التوثيق التقني
│   └── manage.py                  # أداة إدارة Django
│
├── README.md                       # ملف تعريف المشروع
├── CHANGELOG.md                    # سجل التغييرات
├── requirements.txt                # المتطلبات
├── setup.py                        # إعدادات التثبيت
├── Makefile                        # أوامر سريعة
├── .env.example                    # مثال على ملف البيئة
└── .gitignore                      # ملفات Git المستثناة
```

---

## 🛠 طريقة التثبيت والتشغيل (Setup)

### المتطلبات الأساسية
- Python 3.10+
- pip
- virtualenv (مستحسن)

### خطوات التثبيت

1. **إنشاء البيئة الافتراضية:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

2. **تثبيت المتطلبات:**
   ```bash
   pip install -r requirements.txt
   ```

3. **إعداد متغيرات البيئة:**
   ```bash
   cp .env.example .env
   # عدل ملف .env حسب إعداداتك
   ```

4. **تنفيذ Migrations:**
   ```bash
   cd dental_clinic_system
   python manage.py migrate
   ```

5. **إنشاء مستخدم أدمن:**
   ```bash
   python manage.py createsuperuser
   ```

6. **تجميع الملفات الثابتة:**
   ```bash
   python manage.py collectstatic
   ```

7. **تشغيل الخادم:**
   ```bash
   python manage.py runserver
   ```

### استخدام Makefile (أسهل)

```bash
# تثبيت كامل
make setup

# تشغيل الخادم
make run

# إنشاء superuser
make createsuperuser

# تنظيف الملفات المؤقتة
make clean
```

---

## 🔗 روابط المشروع

بعد تشغيل الخادم:

- **الواجهة الرئيسية:** http://127.0.0.1:8000/
- **لوحة الإدارة:** http://127.0.0.1:8000/admin/
- **توثيق API (Swagger):** http://127.0.0.1:8000/api/docs/

---

## 📦 التقنيات المستخدمة

- **Backend:** Django 5.0, Django REST Framework
- **Frontend:** Bootstrap 5, Vanilla JavaScript
- **Database:** SQLite (قابل للترقية)
- **API Docs:** drf-spectacular (Swagger/OpenAPI)
- **Static Files:** WhiteNoise
- **Environment:** python-dotenv

---

## 🔧 إعدادات الإنتاج

قبل النشر في بيئة الإنتاج، تأكد من:

1. تعيين `DEBUG=False` في ملف `.env`
2. استخدام `SECRET_KEY` قوي وعشوائي
3. تعديل `ALLOWED_HOSTS` باسم النطاق الخاص بك
4. استخدام PostgreSQL بدلاً من SQLite
5. إعداد خادم الويب (Nginx/Apache) مع Gunicorn
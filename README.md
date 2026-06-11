# 🦷 Dental Clinic Management System | نظام إدارة عيادة الأسنان

نظام متكامل لإدارة عيادات الأسنان، مصمم لتوفير تجربة مستخدم سريعة وآمنة.

**📚 Documentation:** [Installation Guide](INSTALLATION.md) | [API Docs](API_DOCUMENTATION.md) | [Project Structure](PROJECT_STRUCTURE.md) | [Changelog](CHANGELOG.md) | [Contributing](CONTRIBUTING.md)

## ✨ الميزات الرئيسية

- **لوحة تحكم عصرية** - واجهة مستخدم تعتمد على الوضع الليلي (Dark Mode)
- **نظام أمان متقدم** - تسجيل دخول وخروج محمي بالكامل مع إدارة صلاحيات
- **البحث اللحظي** - ميزة البحث السريع عن المرضى والمواعيد
- **توثيق API تفاعلي** - Swagger UI لعرض واختبار الروابط برمجياً

## 🏗 بنية المشروع

```
dental_CAS/
├── 📁 dental_clinic_system/     # المشروع الرئيسي (Django)
│   ├── 📁 accounts/              # إدارة المستخدمين + Commands
│   ├── 📁 patients/              # إدارة المرضى
│   ├── 📁 doctors/               # إدارة الأطباء
│   ├── 📁 appointments/          # إدارة المواعيد
│   ├── 📁 config/                # إعدادات Django
│   ├── 📁 templates/             # قوالب HTML (base, accounts)
│   ├── 📁 static/                # CSS, JS, Images
│   ├── 📁 media/                 # ملفات المستخدمين
│   ├── 📁 utils/                 # Middleware, Validators, Helpers
│   ├── 📄 docs.md                # التوثيق التقني
│   ├── 📄 requirements.txt       # المتطلبات
│   ├── 📄 Dockerfile             # Docker إعدادات
│   └── 🔨 manage.py              # أداة إدارة Django
│
├── 📄 README.md                   # تعريف المشروع
├── 📄 INSTALLATION.md             # دليل التثبيت الكامل
├── 📄 API_DOCUMENTATION.md        # توثيق API مفصل
├── 📄 PROJECT_STRUCTURE.md        # هيكل المشروع
├── 📄 CONTRIBUTING.md             # دليل المساهمة
├── 📄 CHANGELOG.md                # سجل التغييرات
├── 📄 LICENSE                     # ترخيص MIT
├── ⚙️  .env.example               # مثال الإعدادات
├── ⚙️  .gitignore                 # إعدادات Git
├── 🔧 Makefile                    # أوامر سريعة
├── 🔧 setup.py                    # إعدادات Python
├── 🐳 docker-compose.yml          # Docker Compose
└── 📁 scripts/                    # سكريبتات التثبيت والنسخ
    ├── setup.sh                   # Linux/Mac setup
    ├── setup.bat                  # Windows setup
    └── backup.sh                  # نسخ احتياطي
```

## 🚀 طريقة التشغيل

1. **إنشاء البيئة الافتراضية:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

2. **تثبيت المتطلبات:**
   ```bash
   pip install -r requirements.txt
   ```

3. **تشغيل migrations:**
   ```bash
   python manage.py migrate
   ```

4. **إنشاء مستخدم أدمن:**
   ```bash
   python manage.py createsuperuser
   ```

5. **تشغيل الخادم:**
   ```bash
   python manage.py runserver
   ```

6. **الوصول للنظام:**
   - الواجهة الرئيسية: http://127.0.0.1:8000/
   - لوحة الإدارة: http://127.0.0.1:8000/admin/
   - توثيق API: http://127.0.0.1:8000/api/docs/

## 🔧 المتطلبات

- Python 3.10+
- Django 5.0+
- SQLite (يمكن ترقيته لـ PostgreSQL/MySQL)

## 👥 المساهمون

- تم تطويره بواسطة فريق Dental Pro

## 📄 الترخيص

MIT License

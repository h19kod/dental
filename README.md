# 🦷 Dental Clinic Management System | نظام إدارة عيادة الأسنان

نظام متكامل لإدارة عيادات الأسنان، مصمم لتوفير تجربة مستخدم سريعة وآمنة.

**📚 Documentation:** [Installation Guide](INSTALLATION.md) | [API Docs](API_DOCUMENTATION.md) | [Changelog](CHANGELOG.md)

## ✨ الميزات الرئيسية

- **لوحة تحكم عصرية** - واجهة مستخدم تعتمد على الوضع الليلي (Dark Mode)
- **نظام أمان متقدم** - تسجيل دخول وخروج محمي بالكامل مع إدارة صلاحيات
- **البحث اللحظي** - ميزة البحث السريع عن المرضى والمواعيد
- **توثيق API تفاعلي** - Swagger UI لعرض واختبار الروابط برمجياً

## 🏗 بنية المشروع

```
dental_CAS/
├── dental_clinic_system/    # المشروع الرئيسي
│   ├── accounts/             # تطبيق إدارة المستخدمين
│   ├── patients/             # تطبيق إدارة المرضى
│   ├── doctors/              # تطبيق إدارة الأطباء
│   ├── appointments/         # تطبيق إدارة المواعيد
│   ├── config/               # إعدادات Django
│   ├── templates/            # قوالب HTML
│   ├── static/               # ملفات CSS, JS, Images
│   ├── media/                # ملفات المستخدمين
│   ├── utils/                # أدوات مساعدة
│   ├── docs.md               # التوثيق التقني
│   ├── requirements.txt      # المتطلبات
│   └── manage.py             # أداة إدارة Django
│
├── README.md                  # ملف تعريف المشروع
├── INSTALLATION.md            # دليل التثبيت الكامل
├── API_DOCUMENTATION.md       # توثيق الـ API
├── CHANGELOG.md               # سجل التغييرات
├── .env.example               # مثال على الإعدادات
├── Makefile                   # أوامر سريعة
└── setup.py                   # إعدادات التثبيت
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

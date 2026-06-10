from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# تسجيل الموديل ليظهر في لوحة التحكم
admin.site.register(User, UserAdmin)
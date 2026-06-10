from django.db import models
from django.conf import settings
from utils.validators import validate_iraqi_phone


class Patient(models.Model):
    # ربط المريض بحساب مستخدم (اختياري إذا كنت تريد للمريض تسجيل دخول)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='patient_profile'
    )
    age = models.PositiveIntegerField(verbose_name="العمر")
    phone_number = models.CharField(
        max_length=15, 
        validators=[validate_iraqi_phone],
        verbose_name="رقم الهاتف"
    )
    medical_history = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="التاريخ المرضي"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    class Meta:
        verbose_name = "مريض"
        verbose_name_plural = "المرضى"
        ordering = ['-created_at']

    def __str__(self):
        return self.user.get_full_name() or self.user.username
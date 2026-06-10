from django.db import models
from django.conf import settings
from utils.validators import validate_working_hours


class Doctor(models.Model):
    # ربط الطبيب بحساب مستخدم
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='doctor_profile'
    )
    specialization = models.CharField(max_length=100, verbose_name="التخصص")
    bio = models.TextField(blank=True, null=True, verbose_name="نبذة تعريفية")
    working_hours = models.CharField(
        max_length=200, 
        validators=[validate_working_hours],
        help_text="مثال: 9 ص - 5 م",
        verbose_name="ساعات العمل"
    )
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    class Meta:
        verbose_name = "طبيب"
        verbose_name_plural = "الأطباء"
        ordering = ['-created_at']

    def __str__(self):
        return f"د. {self.user.get_full_name() or self.user.username} - {self.specialization}"
    
    @property
    def full_name(self):
        return f"د. {self.user.get_full_name() or self.user.username}"
    
    @property
    def total_appointments(self):
        return self.appointments.count()
    
    @property
    def today_appointments(self):
        from django.utils import timezone
        return self.appointments.filter(date=timezone.now().date()).count()
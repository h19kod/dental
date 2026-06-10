from django.db import migrations, models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # تعريف أنواع المستخدمين كخيارات ثابتة
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        DOCTOR = "DOCTOR", "Doctor"
        RECEPTIONIST = "RECEPTIONIST", "Receptionist"
        PATIENT = "PATIENT", "Patient"

    # الحقل الأساسي لتحديد نوع المستخدم
    role = models.CharField(
        max_length=20, 
        choices=Role.choices, 
        default=Role.ADMIN
    )
    
    # حقول إضافية عامة
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.role}"
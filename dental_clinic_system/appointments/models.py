from django.db import models
from django.core.exceptions import ValidationError
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    # الخيارات المتاحة لحالة الحجز
    STATUS_CHOICES = [
        ('PENDING', 'قيد الانتظار'),
        ('CONFIRMED', 'تم التأكيد'),
        ('COMPLETED', 'تمت الزيارة'),
        ('CANCELLED', 'ملغي'),
    ]

    patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE, 
        related_name='appointments',
        verbose_name="المريض"
    )
    doctor = models.ForeignKey(
        Doctor, 
        on_delete=models.CASCADE, 
        related_name='appointments',
        verbose_name="الطبيب"
    )
    date = models.DateField(verbose_name="التاريخ")
    time = models.TimeField(verbose_name="الوقت")
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='PENDING',
        verbose_name="حالة الحجز"
    )
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات طبية")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # ترتيب المواعيد: الأحدث يظهر أولاً
        ordering = ['-date', '-time']
        # منع تكرار نفس الطبيب في نفس الوقت والتاريخ (Constraint احترافي)
        unique_together = ('doctor', 'date', 'time')
        verbose_name = "حجز"
        verbose_name_plural = "الحجوزات"

    def __str__(self):
        return f"موعد {self.patient} مع د. {self.doctor} بتاريخ {self.date}"

    def clean(self):
        """
        منطق إضافي للتحقق من صحة البيانات قبل الحفظ
        """
        # التأكد من عدم حجز موعد في الماضي (اختياري حسب رغبتك)
        from django.utils import timezone
        if self.date < timezone.now().date():
            raise ValidationError("لا يمكن حجز موعد في تاريخ قديم.")

        # التحقق من تضارب المواعيد (Double check)
        conflicting_appointments = Appointment.objects.filter(
            doctor=self.doctor,
            date=self.date,
            time=self.time
        ).exclude(pk=self.pk) # استثناء الموعد الحالي عند التعديل

        if conflicting_appointments.exists():
            raise ValidationError(f"الطبيب {self.doctor} لديه حجز آخر في هذا الوقت.")
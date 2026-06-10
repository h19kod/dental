from rest_framework import serializers
from .models import Appointment
from doctors.serializers import DoctorSerializer
from patients.serializers import PatientSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    # عرض تفاصيل الطبيب والمريض (للقراءة فقط)
    doctor_detail = DoctorSerializer(source='doctor', read_only=True)
    patient_detail = PatientSerializer(source='patient', read_only=True)
    
    # حقول إضافية لتسهيل العرض في الواجهة
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'id', 'patient', 'doctor', 'patient_detail', 'doctor_detail', 
            'date', 'time', 'status', 'status_display', 'notes'
        ]

    def validate(self, data):
        """
        تحقق إضافي على مستوى السيريالايزر لمنع تعارض المواعيد
        """
        # التأكد من أن الطبيب ليس لديه حجز في نفس الوقت
        exists = Appointment.objects.filter(
            doctor=data['doctor'],
            date=data['date'],
            time=data['time']
        ).exists()
        
        if exists:
            raise serializers.ValidationError("هذا الطبيب لديه موعد آخر في نفس الوقت المحدد.")
        return data
from rest_framework import serializers
from .models import Doctor
from accounts.serializers import UserSerializer
from utils.validators import validate_working_hours


class DoctorSerializer(serializers.ModelSerializer):
    # لجلب بيانات المستخدم كاملة داخل الطبيب
    user = UserSerializer(read_only=True)
    full_name = serializers.CharField(source='full_name', read_only=True)
    total_appointments = serializers.IntegerField(source='total_appointments', read_only=True)
    today_appointments = serializers.IntegerField(source='today_appointments', read_only=True)
    
    class Meta:
        model = Doctor
        fields = [
            'id', 'user', 'full_name', 'specialization', 'bio', 
            'working_hours', 'is_active', 'total_appointments', 
            'today_appointments', 'created_at'
        ]
        read_only_fields = ['created_at']
    
    def validate_working_hours(self, value):
        validate_working_hours(value)
        return value


class DoctorListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for list views
    """
    full_name = serializers.CharField(source='full_name', read_only=True)
    
    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'specialization', 'is_active']
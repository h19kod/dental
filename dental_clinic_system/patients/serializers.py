from rest_framework import serializers
from .models import Patient
from accounts.serializers import UserSerializer
from utils.validators import validate_iraqi_phone, validate_name


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'id', 'user', 'full_name', 'email', 'age', 
            'phone_number', 'medical_history', 'created_at'
        ]
        read_only_fields = ['created_at']
    
    def validate_phone_number(self, value):
        if value:
            validate_iraqi_phone(value)
        return value
    
    def validate_age(self, value):
        if value < 0 or value > 150:
            raise serializers.ValidationError("العمر يجب أن يكون بين 0 و 150 سنة")
        return value


class PatientCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new patient with user
    """
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True, required=False)
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password',
            'age', 'phone_number', 'medical_history'
        ]
    
    def validate_username(self, value):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("اسم المستخدم موجود مسبقاً")
        return value
    
    def create(self, validated_data):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Create user
        user_data = {
            'username': validated_data.pop('username'),
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'email': validated_data.pop('email', ''),
            'role': 'PATIENT'
        }
        password = validated_data.pop('password')
        
        user = User.objects.create_user(**user_data)
        user.set_password(password)
        user.save()
        
        # Create patient profile
        patient = Patient.objects.create(user=user, **validated_data)
        return patient
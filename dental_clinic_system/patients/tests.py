from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from patients.models import Patient
from utils.validators import validate_iraqi_phone

User = get_user_model()


class PatientModelTest(TestCase):
    """Tests for Patient model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testpatient',
            password='testpass123',
            role='PATIENT',
            first_name='Test',
            last_name='Patient'
        )
    
    def test_patient_creation(self):
        """Test patient profile is created correctly"""
        patient = Patient.objects.create(
            user=self.user,
            age=30,
            phone_number='07701234567',
            medical_history='No history'
        )
        
        self.assertEqual(patient.user, self.user)
        self.assertEqual(patient.age, 30)
        self.assertEqual(patient.phone_number, '07701234567')
        self.assertEqual(str(patient), 'Test Patient')
    
    def test_patient_phone_validation(self):
        """Test phone number validation"""
        # Valid Iraqi phone numbers
        valid_numbers = ['07701234567', '07801234567', '07901234567']
        for number in valid_numbers:
            try:
                validate_iraqi_phone(number)
            except ValidationError:
                self.fail(f"{number} should be valid")
        
        # Invalid phone numbers
        invalid_numbers = ['12345', 'abc', '0770123456']
        for number in invalid_numbers:
            with self.assertRaises(ValidationError):
                validate_iraqi_phone(number)
    
    def test_patient_ordering(self):
        """Test patients are ordered by creation date"""
        user1 = User.objects.create_user(
            username='patient1', password='test123', role='PATIENT'
        )
        user2 = User.objects.create_user(
            username='patient2', password='test123', role='PATIENT'
        )
        
        patient1 = Patient.objects.create(
            user=user1, age=25, phone_number='07701234567'
        )
        patient2 = Patient.objects.create(
            user=user2, age=30, phone_number='07801234567'
        )
        
        patients = list(Patient.objects.all())
        self.assertEqual(patients[0], patient2)  # Most recent first
        self.assertEqual(patients[1], patient1)


class PatientSerializerTest(TestCase):
    """Tests for Patient serializers"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testpatient',
            password='testpass123',
            role='PATIENT',
            first_name='Test',
            last_name='Patient'
        )
    
    def test_patient_age_validation(self):
        """Test age must be reasonable"""
        from patients.serializers import PatientSerializer
        
        # Valid age
        serializer = PatientSerializer(data={
            'age': 30,
            'phone_number': '07701234567'
        })
        self.assertTrue(serializer.is_valid())
        
        # Invalid age (too high)
        serializer = PatientSerializer(data={
            'age': 200,
            'phone_number': '07701234567'
        })
        self.assertFalse(serializer.is_valid())
        self.assertIn('age', serializer.errors)

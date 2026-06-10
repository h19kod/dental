from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import date, time
from django.utils import timezone

from doctors.models import Doctor
from appointments.models import Appointment
from patients.models import Patient
from utils.validators import validate_working_hours

User = get_user_model()


class DoctorModelTest(TestCase):
    """Tests for Doctor model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testdoctor',
            password='testpass123',
            role='DOCTOR',
            first_name='Test',
            last_name='Doctor'
        )
    
    def test_doctor_creation(self):
        """Test doctor profile is created correctly"""
        doctor = Doctor.objects.create(
            user=self.user,
            specialization='طبيب أسنان عام',
            bio='Expert dentist with 10 years experience',
            working_hours='9 ص - 5 م',
            is_active=True
        )
        
        self.assertEqual(doctor.user, self.user)
        self.assertEqual(doctor.specialization, 'طبيب أسنان عام')
        self.assertEqual(doctor.working_hours, '9 ص - 5 م')
        self.assertTrue(doctor.is_active)
        self.assertEqual(str(doctor), 'د. Test Doctor - طبيب أسنان عام')
    
    def test_doctor_full_name_property(self):
        """Test full_name property"""
        doctor = Doctor.objects.create(
            user=self.user,
            specialization='جراحة أسنان',
            working_hours='10 ص - 6 م'
        )
        
        self.assertEqual(doctor.full_name, 'د. Test Doctor')
    
    def test_doctor_working_hours_validation(self):
        """Test working hours format validation"""
        # Valid formats
        valid_hours = ['9 ص - 5 م', '10 AM - 6 PM', '8 ص - 4 م']
        for hours in valid_hours:
            try:
                validate_working_hours(hours)
            except ValidationError:
                self.fail(f"'{hours}' should be valid")
        
        # Invalid formats
        invalid_hours = ['9 to 5', 'invalid', '25 ص - 5 م']
        for hours in invalid_hours:
            with self.assertRaises(ValidationError):
                validate_working_hours(hours)
    
    def test_doctor_appointment_properties(self):
        """Test appointment count properties"""
        doctor = Doctor.objects.create(
            user=self.user,
            specialization='تقويم الأسنان',
            working_hours='9 ص - 5 م'
        )
        
        # Create patient
        patient_user = User.objects.create_user(
            username='testpatient',
            password='testpass123',
            role='PATIENT'
        )
        patient = Patient.objects.create(
            user=patient_user,
            age=25,
            phone_number='07701234567'
        )
        
        # Initially no appointments
        self.assertEqual(doctor.total_appointments, 0)
        self.assertEqual(doctor.today_appointments, 0)
        
        # Create appointments
        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date=timezone.now().date() + timezone.timedelta(days=1),
            time=time(10, 0)
        )
        
        # Check total appointments
        self.assertEqual(doctor.total_appointments, 1)
    
    def test_doctor_ordering(self):
        """Test doctors are ordered by creation date"""
        user1 = User.objects.create_user(
            username='doctor1', password='test123', role='DOCTOR'
        )
        user2 = User.objects.create_user(
            username='doctor2', password='test123', role='DOCTOR'
        )
        
        doctor1 = Doctor.objects.create(
            user=user1, specialization='طب عام', working_hours='9 ص - 5 م'
        )
        doctor2 = Doctor.objects.create(
            user=user2, specialization='جراحة', working_hours='10 ص - 6 م'
        )
        
        doctors = list(Doctor.objects.all())
        self.assertEqual(doctors[0], doctor2)  # Most recent first
        self.assertEqual(doctors[1], doctor1)

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import date, time, timedelta
from django.utils import timezone

from appointments.models import Appointment
from patients.models import Patient
from doctors.models import Doctor

User = get_user_model()


class AppointmentModelTest(TestCase):
    """Tests for Appointment model"""
    
    def setUp(self):
        # Create test users
        self.patient_user = User.objects.create_user(
            username='testpatient',
            password='testpass123',
            role='PATIENT',
            first_name='Test',
            last_name='Patient'
        )
        self.doctor_user = User.objects.create_user(
            username='testdoctor',
            password='testpass123',
            role='DOCTOR',
            first_name='Test',
            last_name='Doctor'
        )
        
        # Create patient and doctor profiles
        self.patient = Patient.objects.create(
            user=self.patient_user,
            age=30,
            phone_number='07701234567'
        )
        self.doctor = Doctor.objects.create(
            user=self.doctor_user,
            specialization='طبيب أسنان عام',
            working_hours='9 ص - 5 م'
        )
    
    def test_appointment_creation(self):
        """Test appointment is created correctly"""
        appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            date=timezone.now().date() + timedelta(days=1),
            time=time(10, 0),
            status='PENDING',
            notes='فحص دوري'
        )
        
        self.assertEqual(appointment.patient, self.patient)
        self.assertEqual(appointment.doctor, self.doctor)
        self.assertEqual(appointment.status, 'PENDING')
        self.assertTrue(appointment.notes, 'فحص دوري')
    
    def test_appointment_str_representation(self):
        """Test appointment string representation"""
        appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            date=timezone.now().date() + timedelta(days=1),
            time=time(10, 0)
        )
        
        expected = f"موعد {self.patient} مع د. {self.doctor} بتاريخ {appointment.date}"
        self.assertEqual(str(appointment), expected)
    
    def test_unique_together_constraint(self):
        """Test that doctor cannot have two appointments at same time"""
        appointment_date = timezone.now().date() + timedelta(days=1)
        appointment_time = time(10, 0)
        
        # Create first appointment
        Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            date=appointment_date,
            time=appointment_time
        )
        
        # Try to create second appointment at same time
        with self.assertRaises(Exception):  # Should raise IntegrityError
            Appointment.objects.create(
                patient=self.patient,
                doctor=self.doctor,
                date=appointment_date,
                time=appointment_time
            )
    
    def test_appointment_validation_future_date(self):
        """Test appointment cannot be in the past"""
        with self.assertRaises(Exception):
            Appointment.objects.create(
                patient=self.patient,
                doctor=self.doctor,
                date=timezone.now().date() - timedelta(days=1),  # Past date
                time=time(10, 0)
            )


class AppointmentAPITest(TestCase):
    """Tests for Appointment API"""
    
    def setUp(self):
        self.client = Client()
        
        # Create admin user
        self.admin_user = User.objects.create_user(
            username='admin',
            password='admin123',
            role='ADMIN'
        )
        
        # Create patient and doctor
        self.patient_user = User.objects.create_user(
            username='patient1',
            password='patient123',
            role='PATIENT'
        )
        self.doctor_user = User.objects.create_user(
            username='doctor1',
            password='doctor123',
            role='DOCTOR'
        )
        
        self.patient = Patient.objects.create(
            user=self.patient_user,
            age=25,
            phone_number='07701234567'
        )
        self.doctor = Doctor.objects.create(
            user=self.doctor_user,
            specialization='جراحة أسنان',
            working_hours='9 ص - 5 م'
        )
    
    def test_api_appointments_list(self):
        """Test API returns appointments list"""
        self.client.login(username='admin', password='admin123')
        
        # Create test appointment
        Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            date=timezone.now().date() + timedelta(days=1),
            time=time(10, 0)
        )
        
        response = self.client.get('/api/appointments/')
        self.assertEqual(response.status_code, 200)
        
        import json
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
    
    def test_api_appointments_search(self):
        """Test API search functionality"""
        self.client.login(username='admin', password='admin123')
        
        # Create appointment
        Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            date=timezone.now().date() + timedelta(days=1),
            time=time(10, 0)
        )
        
        # Search by patient username
        response = self.client.get('/api/appointments/?search=patient1')
        self.assertEqual(response.status_code, 200)
        
        import json
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
    
    def test_api_appointment_delete(self):
        """Test API delete appointment"""
        self.client.login(username='admin', password='admin123')
        
        # Create and then delete appointment
        appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            date=timezone.now().date() + timedelta(days=1),
            time=time(10, 0)
        )
        
        response = self.client.delete(f'/api/appointments/{appointment.id}/')
        self.assertEqual(response.status_code, 200)
        
        # Verify appointment is deleted
        self.assertEqual(Appointment.objects.count(), 0)

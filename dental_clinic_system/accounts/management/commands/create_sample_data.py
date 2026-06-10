"""
Management command to create sample data for testing
"""
import random
from datetime import date, time, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

from accounts.models import User
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment


class Command(BaseCommand):
    help = 'Creates sample data for testing the dental clinic system'

    def add_arguments(self, parser):
        parser.add_argument(
            '--patients',
            type=int,
            default=10,
            help='Number of sample patients to create'
        )
        parser.add_argument(
            '--doctors',
            type=int,
            default=5,
            help='Number of sample doctors to create'
        )
        parser.add_argument(
            '--appointments',
            type=int,
            default=20,
            help='Number of sample appointments to create'
        )

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING('Creating sample data...'))
        
        num_patients = options['patients']
        num_doctors = options['doctors']
        num_appointments = options['appointments']
        
        # Create admin if doesn't exist
        if not User.objects.filter(username='admin').exists():
            self.create_admin()
        
        # Create doctors
        doctors = self.create_doctors(num_doctors)
        
        # Create patients
        patients = self.create_patients(num_patients)
        
        # Create appointments
        self.create_appointments(patients, doctors, num_appointments)
        
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created {num_doctors} doctors, '
            f'{num_patients} patients, and {num_appointments} appointments!'
        ))
    
    def create_admin(self):
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@dental.com',
            password='admin123',
            first_name='مدير',
            last_name='النظام',
            role='ADMIN'
        )
        self.stdout.write(f'  Created admin user: {admin.username}')
    
    def create_doctors(self, count):
        doctors = []
        specializations = [
            'طبيب أسنان عام',
            'جراح فم وفكين',
            'تقويم الأسنان',
            'علاج جذور الأسنان',
            'ترميم الأسنان',
            'طب أسنان الأطفال'
        ]
        
        working_hours_options = [
            '9 ص - 5 م',
            '10 ص - 6 م',
            '8 ص - 4 م',
            '12 م - 8 م'
        ]
        
        for i in range(count):
            user = User.objects.create_user(
                username=f'doctor{i+1}',
                email=f'doctor{i+1}@dental.com',
                password='doctor123',
                first_name=f'دكتور{i+1}',
                last_name='الأسنان',
                role='DOCTOR'
            )
            
            doctor = Doctor.objects.create(
                user=user,
                specialization=random.choice(specializations),
                bio=f'طبيب أسنان متخصص في {random.choice(specializations)} مع خبرة 10 سنوات',
                working_hours=random.choice(working_hours_options),
                is_active=True
            )
            doctors.append(doctor)
            self.stdout.write(f'  Created doctor: {doctor}')
        
        return doctors
    
    def create_patients(self, count):
        patients = []
        first_names = ['أحمد', 'محمد', 'علي', 'خالد', 'عمر', 'يوسف', 'فاطمة', 'مريم', 'سارة', 'ليلى']
        last_names = ['الأحمد', 'المحمد', 'العلي', 'الخالد', 'العمر', 'اليوسف', 'الفاطمة', 'المريم']
        
        for i in range(count):
            user = User.objects.create_user(
                username=f'patient{i+1}',
                email=f'patient{i+1}@email.com',
                password='patient123',
                first_name=random.choice(first_names),
                last_name=random.choice(last_names),
                role='PATIENT'
            )
            
            patient = Patient.objects.create(
                user=user,
                age=random.randint(18, 70),
                phone_number=f'07{random.randint(3, 9)}{random.randint(10000000, 99999999)}',
                medical_history='لا يوجد تاريخ مرضي مهم'
            )
            patients.append(patient)
            self.stdout.write(f'  Created patient: {patient}')
        
        return patients
    
    def create_appointments(self, patients, doctors, count):
        statuses = ['PENDING', 'CONFIRMED', 'COMPLETED', 'CANCELLED']
        status_weights = [0.3, 0.4, 0.2, 0.1]  # More pending and confirmed
        
        # Generate dates for next 30 days
        base_date = date.today()
        
        created_count = 0
        max_attempts = count * 3
        attempts = 0
        
        while created_count < count and attempts < max_attempts:
            attempts += 1
            
            patient = random.choice(patients)
            doctor = random.choice(doctors)
            appointment_date = base_date + timedelta(days=random.randint(0, 30))
            
            # Generate random time between 9 AM and 5 PM
            hour = random.randint(9, 16)
            minute = random.choice([0, 15, 30, 45])
            appointment_time = time(hour, minute)
            
            # Check if slot is available
            if not Appointment.objects.filter(
                doctor=doctor,
                date=appointment_date,
                time=appointment_time
            ).exists():
                
                status = random.choices(statuses, weights=status_weights)[0]
                
                Appointment.objects.create(
                    patient=patient,
                    doctor=doctor,
                    date=appointment_date,
                    time=appointment_time,
                    status=status,
                    notes=f'موعد {created_count + 1} - فحص دوري'
                )
                
                created_count += 1
                if created_count % 5 == 0:
                    self.stdout.write(f'  Created {created_count}/{count} appointments...')
        
        self.stdout.write(f'  Created {created_count} appointments')

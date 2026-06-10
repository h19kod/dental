"""
Setup script for Dental Clinic System
"""
from setuptools import setup, find_packages

setup(
    name='dental-clinic-system',
    version='1.0.0',
    description='نظام إدارة عيادة الأسنان - Dental Clinic Management System',
    author='Dental Pro Team',
    packages=find_packages(),
    install_requires=[
        'Django==5.0.2',
        'djangorestframework==3.14.0',
        'django-cors-headers==4.3.1',
        'drf-spectacular==0.27.1',
        'Pillow==10.2.0',
        'python-dotenv==1.0.1',
        'whitenoise==6.6.0',
        'gunicorn==21.2.0',
    ],
    python_requires='>=3.10',
)

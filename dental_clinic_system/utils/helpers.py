"""
Helper functions for the Dental Clinic System
"""

from datetime import datetime, date
from django.utils import timezone


def get_today_appointments(appointments_model):
    """
    Get appointments for today
    """
    today = timezone.now().date()
    return appointments_model.objects.filter(date=today)


def get_week_appointments(appointments_model):
    """
    Get appointments for the current week
    """
    today = timezone.now().date()
    start_of_week = today - timezone.timedelta(days=today.weekday())
    end_of_week = start_of_week + timezone.timedelta(days=6)
    return appointments_model.objects.filter(date__range=[start_of_week, end_of_week])


def format_phone_number(phone):
    """
    Format phone number to standard format
    """
    if not phone:
        return ""
    # Remove any non-digit characters
    digits = ''.join(filter(str.isdigit, phone))
    # Add country code if missing
    if len(digits) == 10 and digits.startswith('0'):
        digits = '964' + digits[1:]
    return digits


def get_status_color(status):
    """
    Get Bootstrap color class for appointment status
    """
    colors = {
        'PENDING': 'warning',
        'CONFIRMED': 'info',
        'COMPLETED': 'success',
        'CANCELLED': 'danger',
    }
    return colors.get(status, 'secondary')


def get_status_display(status):
    """
    Get Arabic display text for appointment status
    """
    display = {
        'PENDING': 'قيد الانتظار',
        'CONFIRMED': 'تم التأكيد',
        'COMPLETED': 'تمت الزيارة',
        'CANCELLED': 'ملغي',
    }
    return display.get(status, status)

"""
Custom Validators for Dental Clinic System
"""

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_iraqi_phone(value):
    """
    Validate Iraqi phone number format
    """
    # Remove any spaces or dashes
    phone = re.sub(r'[\s-]', '', value)
    
    # Iraqi phone patterns
    patterns = [
        r'^07[3-9]\d{8}$',      # Mobile: 07x xxxx xxxx
        r'^009647[3-9]\d{8}$',  # International: +9647x xxx xxxx
        r'^\+9647[3-9]\d{8}$',  # International with +
    ]
    
    for pattern in patterns:
        if re.match(pattern, phone):
            return
    
    raise ValidationError(
        _('Invalid Iraqi phone number format. Use: 07x xxx xxxx'),
        params={'value': value},
    )


def validate_name(value):
    """
    Validate name contains only letters and spaces
    """
    if not re.match(r'^[\u0600-\u06FFa-zA-Z\s]+$', value):
        raise ValidationError(
            _('Name should only contain letters and spaces'),
            params={'value': value},
        )


def validate_future_date(value):
    """
    Validate date is not in the past
    """
    from datetime import date
    if value < date.today():
        raise ValidationError(
            _('Date cannot be in the past'),
            params={'value': value},
        )


def validate_working_hours(value):
    """
    Validate working hours format
    Example: 9 ص - 5 م
    """
    pattern = r'^\d{1,2}\s+(ص|م|AM|PM)\s+-\s+\d{1,2}\s+(ص|م|AM|PM)$'
    if not re.match(pattern, value, re.IGNORECASE):
        raise ValidationError(
            _('Invalid working hours format. Use: 9 ص - 5 م or 9 AM - 5 PM'),
            params={'value': value},
        )

"""
Custom Middleware for Dental Clinic System
"""

import logging
from django.http import JsonResponse
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


class SecurityHeadersMiddleware:
    """
    Add security headers to all responses
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Security Headers
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
        
        return response


class RoleBasedAccessMiddleware:
    """
    Middleware to check user roles and restrict access
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # Paths that require specific roles
        self.restricted_paths = {
            '/admin/': ['ADMIN'],
            '/api/doctors/': ['ADMIN', 'DOCTOR', 'RECEPTIONIST'],
        }

    def __call__(self, request):
        if request.user.is_authenticated:
            path = request.path
            
            # Check if path is restricted
            for restricted_path, allowed_roles in self.restricted_paths.items():
                if path.startswith(restricted_path):
                    user_role = getattr(request.user, 'role', None)
                    if user_role not in allowed_roles:
                        logger.warning(
                            f"Access denied: User {request.user.username} with role {user_role} "
                            f"attempted to access {path}"
                        )
                        
                        # Return JSON for API requests
                        if request.headers.get('Accept') == 'application/json':
                            return JsonResponse(
                                {'error': 'Insufficient permissions'}, 
                                status=403
                            )
                        
                        # Redirect for regular requests
                        return redirect('dashboard')
        
        return self.get_response(request)


class RequestLoggingMiddleware:
    """
    Log all requests for monitoring
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log request
        logger.info(
            f"Request: {request.method} {request.path} - "
            f"User: {request.user.username if request.user.is_authenticated else 'Anonymous'} - "
            f"IP: {self.get_client_ip(request)}"
        )
        
        response = self.get_response(request)
        
        # Log response status
        logger.info(f"Response: {response.status_code}")
        
        return response
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class MaintenanceModeMiddleware:
    """
    Middleware to enable maintenance mode
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.maintenance_mode = False  # Set to True to enable maintenance mode

    def __call__(self, request):
        if self.maintenance_mode and not request.user.is_superuser:
            if request.headers.get('Accept') == 'application/json':
                return JsonResponse(
                    {'error': 'System is under maintenance'}, 
                    status=503
                )
            return redirect('/maintenance/')
        
        return self.get_response(request)

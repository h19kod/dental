from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):
    """Tests for the custom User model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            role='ADMIN'
        )
    
    def test_user_creation(self):
        """Test user is created correctly"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.role, 'ADMIN')
        self.assertTrue(self.user.check_password('testpass123'))
    
    def test_user_str_representation(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), 'testuser - ADMIN')
    
    def test_role_choices(self):
        """Test role choices are valid"""
        valid_roles = ['ADMIN', 'DOCTOR', 'RECEPTIONIST', 'PATIENT']
        for role in valid_roles:
            user = User.objects.create_user(
                username=f'test_{role.lower()}',
                password='testpass123',
                role=role
            )
            self.assertEqual(user.role, role)


class AuthenticationTest(TestCase):
    """Tests for authentication views"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            role='ADMIN'
        )
    
    def test_login_view_get(self):
        """Test login page loads"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
    
    def test_login_view_post_valid(self):
        """Test login with valid credentials"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
    
    def test_login_view_post_invalid(self):
        """Test login with invalid credentials"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        # Should stay on login page with error
    
    def test_dashboard_requires_login(self):
        """Test dashboard requires authentication"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_dashboard_accessible_when_logged_in(self):
        """Test dashboard accessible when logged in"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
    
    def test_logout_view(self):
        """Test logout functionality"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout

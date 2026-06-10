from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet

# استخدام الـ Router لتوليد روابط الـ API تلقائياً
router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
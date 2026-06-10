from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # لوحة الإدارة
    path('admin/', admin.site.urls),
    
    # روابط الـ API
    path('api/', include('appointments.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
    
    # توثيق الـ API التفاعلي (Swagger)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # نظام تسجيل الدخول والخروج
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # لوحة التحكم الرئيسية (Dashboard)
    path('', login_required(TemplateView.as_view(template_name='index.html')), name='dashboard'),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
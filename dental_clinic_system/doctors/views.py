from rest_framework import viewsets, permissions
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # الإدمن والريسبشن فقط يمكنهم التعديل، البقية للقراءة فقط
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
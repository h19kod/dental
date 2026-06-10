from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('-date', '-time')
    serializer_class = AppointmentSerializer

    # دعم البحث باسم المريض
    def get_queryset(self):
        queryset = Appointment.objects.all()
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(patient__user__username__icontains=search)
        return queryset

    # رسالة نجاح عند الحذف
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "تم حذف الموعد"}, status=status.HTTP_200_OK)
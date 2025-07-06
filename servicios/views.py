from rest_framework import generics
from cotizaciones.permissions import IsAdminUserCustom
from rest_framework.permissions import AllowAny, IsAuthenticated
from servicios.serializer import ServicioSerializer
from .models import Servicio

class ServicioListView(generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioCreateView(generics.CreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    permission_classes = [IsAdminUserCustom]

class ServicioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    permission_classes = [IsAdminUserCustom]

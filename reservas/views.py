from rest_framework import generics, permissions
from reservas.serializer import ReservaSerializer
from .models import Reserva

# Cliente ve sus reservas
class MisReservasView(generics.ListAPIView):
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reserva.objects.filter(cotizacion__cliente=self.request.user)

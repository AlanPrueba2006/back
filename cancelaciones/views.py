from rest_framework import generics, permissions, status
from rest_framework.response import Response
from cancelaciones.serializer import CancelacionReservaSerializer
from .models import CancelacionReserva
from reservas.models import Reserva
from django.utils.timezone import now

class CancelacionCreateView(generics.CreateAPIView):
    serializer_class = CancelacionReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        reserva_id = request.data.get("reserva_id")
        motivo = request.data.get("motivo_cliente", "")

        try:
            reserva = Reserva.objects.get(id=reserva_id, cotizacion__cliente=request.user)
        except Reserva.DoesNotExist:
            return Response({"error": "Reserva no encontrada."}, status=404)

        if CancelacionReserva.objects.filter(reserva=reserva).exists():
            return Response({"error": "Ya solicitaste cancelación."}, status=400)

        reserva.estado = "cancelacion_solicitada"
        reserva.save()

        cancel = CancelacionReserva.objects.create(
            reserva=reserva,
            motivo_cliente=motivo
        )

        return Response({"mensaje": "Solicitud enviada."})

class AceptarCancelarReservaView(generics.UpdateAPIView):
    queryset = CancelacionReserva.objects.all()
    serializer_class = CancelacionReservaSerializer
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        cancelacion = self.get_object()
        cancelacion.aceptada_por_admin = True
        cancelacion.fecha_respuesta = now()
        cancelacion.save()

        cancelacion.reserva.estado = "cancelada"
        cancelacion.reserva.save()

        return Response({"mensaje": "Cancelación aceptada."})

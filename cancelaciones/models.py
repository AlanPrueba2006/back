from django.db import models
from reservas.models import Reserva

class CancelacionReserva(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    motivo_cliente = models.TextField(blank=True)
    aceptada_por_admin = models.BooleanField(default=False)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_respuesta = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Cancelación solicitada: {self.reserva.cotizacion.cliente.username}"
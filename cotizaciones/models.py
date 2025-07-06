from django.db import models
from django.conf import settings

from servicios.models import Servicio

class Cotizacion(models.Model):
    ESTADOS = [
        ('abierta', 'Abierta'),
        ('pendiente', 'Pendiente de pago'),
        ('pagada', 'Pagada')
    ]

    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipo_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    numero_invitados = models.CharField(max_length=50)
    fecha_evento = models.DateField()
    servicios_adicionales = models.TextField(blank=True)
    mensaje = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='abierta')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    comprobante_pago = models.FileField(upload_to='comprobantes/', null=True, blank=True)

    def __str__(self):
        return f"Cotización de {self.cliente.username} para {self.fecha_evento}"


from django.db import models
from cotizaciones.models import Cotizacion

class Reserva(models.Model):
    cotizacion = models.OneToOneField(Cotizacion, on_delete=models.CASCADE)
    fecha_reservada = models.DateField()
    creada_el = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='confirmada') 

    def __str__(self):
        return f"Reserva de {self.cotizacion.cliente.username}"

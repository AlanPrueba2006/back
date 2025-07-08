from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    tipo_servicio = serializers.CharField(source='cotizacion.tipo_servicio.titulo', read_only=True)
    fecha_evento = serializers.DateField(source='cotizacion.fecha_evento', read_only=True)
    numero_invitados = serializers.CharField(source='cotizacion.numero_invitados', read_only=True)
    precio = serializers.DecimalField(source='cotizacion.precio', read_only=True, max_digits=10, decimal_places=2)
    cliente_username = serializers.CharField(source='cotizacion.cliente.username', read_only=True)

    class Meta:
        model = Reserva
        fields = [
            'id',
            'fecha_reservada',
            'creada_el',
            'estado',
            'cotizacion',
            'tipo_servicio',
            'fecha_evento',
            'numero_invitados',
            'precio',
            'cliente_username',
        ]



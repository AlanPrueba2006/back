from rest_framework import serializers

from reservas.serializer import ReservaSerializer
from .models import CancelacionReserva

class CancelacionReservaSerializer(serializers.ModelSerializer):
    reserva = ReservaSerializer(read_only=True)

    class Meta:
        model = CancelacionReserva
        fields = '__all__'
        read_only_fields = ['fecha_solicitud', 'fecha_respuesta', 'reserva']


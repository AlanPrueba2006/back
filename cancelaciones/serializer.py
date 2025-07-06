from rest_framework import serializers
from .models import CancelacionReserva

class CancelacionReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancelacionReserva
        fields = '__all__'
        read_only_fields = ['fecha_solicitud', 'fecha_respuesta']

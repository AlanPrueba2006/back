from rest_framework import serializers

from servicios.models import Servicio
from .models import Cotizacion

class CotizacionSerializer(serializers.ModelSerializer):
    tipo_servicio = serializers.StringRelatedField(read_only=True) 
    tipo_servicio_id = serializers.PrimaryKeyRelatedField(
        source='tipo_servicio',
        queryset=Servicio.objects.all(),
        write_only=True
    )

    class Meta:
        model = Cotizacion
        fields = '__all__'
        read_only_fields = ['cliente', 'estado', 'fecha_creacion']



class CotizacionAdminUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = ['precio', 'estado']

class ComprobantePagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = ['comprobante_pago']

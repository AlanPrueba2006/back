from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from cotizaciones.serializer import ComprobantePagoSerializer, CotizacionAdminUpdateSerializer, CotizacionSerializer
from .models import Cotizacion

class CotizacionCreateView(generics.CreateAPIView):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(cliente=self.request.user)

class CotizacionesListView(generics.ListAPIView):
    serializer_class = CotizacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cotizacion.objects.filter(cliente=self.request.user)



class CotizacionesAdminListView(generics.ListAPIView):
    """ Devuelve todas las cotizaciones solo para usuarios con rol admin. """
    serializer_class = CotizacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.rol == 'admin':
            return Cotizacion.objects.all().order_by('-fecha_creacion')
        return Cotizacion.objects.none()


class CotizacionUpdateView(generics.UpdateAPIView):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionAdminUpdateSerializer
    permission_classes = [IsAuthenticated]
    
class CotizacionComprobanteView(generics.UpdateAPIView):
    queryset = Cotizacion.objects.all()
    serializer_class = ComprobantePagoSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):  # <-- ESTO ES CLAVE
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        cotizacion = self.get_object()

        if cotizacion.cliente != request.user:
            return Response({'error': 'No autorizado.'}, status=403)

        archivo = request.FILES.get('comprobante_pago')
        if not archivo:
            return Response({"error": "Debes subir una imagen o PDF."}, status=400)

        cotizacion.comprobante_pago = archivo
        cotizacion.estado = 'pagada'
        cotizacion.save()

        try:
            from reservas.models import Reserva
            Reserva.objects.create(
                cotizacion=cotizacion,
                fecha_reservada=cotizacion.fecha_evento
            )
        except Exception as e:
            return Response({"error": f"Error al crear la reserva: {str(e)}"}, status=500)

        return Response({"mensaje": "Pago subido y reserva creada."}, status=200)


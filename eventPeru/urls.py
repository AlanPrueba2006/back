"""
URL configuration for eventPeru project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf.urls.static import static

from cancelaciones.views import AceptarCancelarReservaView, CancelacionCreateView, CancelacionesPendientesAdminView
from cotizaciones.views import CotizacionComprobanteView, CotizacionCreateView, CotizacionUpdateView, CotizacionesAdminListView, CotizacionesListView
from reservas.views import ReservasAdminView, ReservasListView
from servicios.views import ServicioCreateView, ServicioDetailView, ServicioListView
from usuarios.views import DecryptUserView, LoginView, RegisterView, UsuarioChangeStateView, UsuarioDeleteView, UsuarioDetailView, UsuarioListView, UsuarioUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('usuarios/register/', RegisterView.as_view(), name='usuario-register'),
    path('usuarios/login/', LoginView.as_view(), name='usuario-login'),
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<str:dni>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('usuarios/<str:dni>/update/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('usuarios/<str:dni>/change-state/', UsuarioChangeStateView.as_view(), name='usuario-change-state'),
    path('usuarios/<str:dni>/delete/', UsuarioDeleteView.as_view(), name='usuario-delete'),
    path('decrypt-user/', DecryptUserView.as_view(), name='decrypt-user'),

    # servicios
    path('servicios/', ServicioListView.as_view(), name='listar-servicios'),
    path('servicios/create/', ServicioCreateView.as_view(), name='crear-servicio'),
    path('servicios/<int:pk>/', ServicioDetailView.as_view(), name='detalle-servicio'),

    # cotizaciones
    path('cotizacion/create/', CotizacionCreateView.as_view(), name='crear-cotizacion'),
    path('cotizacion/', CotizacionesListView.as_view(), name='mis-cotizaciones'),
    path('cotizacion/<int:pk>/precio/', CotizacionUpdateView.as_view(), name='editar-cotizacion'),
    path('cotizacion/<int:pk>/pago/', CotizacionComprobanteView.as_view(), name='subir-comprobante'),
    path('cotizacion/admin/', CotizacionesAdminListView.as_view(), name='cotizaciones-admin'),

    #reservas
    path('reservas/', ReservasListView.as_view(), name='mis-reservas'),
    path('reservas/admin/', ReservasAdminView.as_view()),

    #cancelaciones
    path('solicitar-cancelacion/', CancelacionCreateView.as_view(), name='solicitar-cancelacion'),
    path('cancelaciones/admin/', CancelacionesPendientesAdminView.as_view()),
    path('cancelacion/<int:pk>/aceptar/', AceptarCancelarReservaView.as_view(), name='aceptar-cancelacion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

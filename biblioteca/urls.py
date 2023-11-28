from django.urls import path
from nastu_site import settings
from . import views
from .views import *
from django.conf.urls import static

urlpatterns = [
    path('', ListaLibros.as_view(), name='lista_libros'),
    path('añadir/', CrearLibro.as_view(), name='anadir_libro'),
    path('editar/<int:pk>', ActualizarLibro.as_view(), name='editar_libro'),
    path('detalle/<int:pk>', DetallesLibro.as_view(), name='detalle'),
    path('borrar_libro/<int:pk>', BorrarLibro.as_view(), name='borrar_libro'),
]

"""
urlpatterns+=[(static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))]
"""

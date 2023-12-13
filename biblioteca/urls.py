from django.urls import path
from .views import *


urlpatterns = [
    path('', ListaLibros.as_view(), name='lista_libros'),
    path('añadir/', CrearLibro.as_view(), name='anadir_libro'),
    path('editar/<int:pk>', ActualizarLibro.as_view(), name='editar_libro'),
    path('detalle/<int:pk>', DetallesLibro.as_view(), name='detalle'),
    path('borrar/<int:pk>', BorrarLibro.as_view(), name='borrar_libro'),
    path('reservar/<int:pk>', ReservarLibro.as_view(), name='reservar_libro'),
    path('devolver/<int:pk>', DevolverLibro.as_view(), name='devolver_libro'),
    path('misLibros/', ListaMisLibros.as_view(), name='mis_libros'),
    path('bestSellers/', ListaBestSellers.as_view(), name='bestSellers'),
]

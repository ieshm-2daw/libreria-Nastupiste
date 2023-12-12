from datetime import date
from typing import Any
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import *
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django .urls import reverse_lazy
# Create your views here.


class ListaLibros(ListView):
    model = Libro
    template_name = 'lista_libros.html'

# queryset=Libro.objects.filter(disponibilidad='disponible')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['libros_disponibles'] = Libro.objects.filter(
            disponibilidad='disponible')
        context['libros_prestados'] = Libro.objects.filter(
            disponibilidad='prestado')
        return context


class ListaMisLibros(ListView):
    model = Libro
    template_name = 'mis_libros.html'
    queryset = Libro.objects.filter(disponibilidad='prestado')


class DevolverLibro(View):
    def get(self, request, pk):
        libro_prestado = get_object_or_404(Libro, pk=pk)
        return render(request, 'devolver_libro.html', {'libro': libro_prestado})

    def post(self, request, pk):
        libro_prestado = get_object_or_404(Libro, pk=pk)
        prestamo = get_object_or_404(Prestamo,
                                     libroPrestado=libro_prestado, usuario=request.user, estado='prestado')
        # Actualizar el estado del préstamos a devuelto:
        prestamo.estado = 'devuelto'
        prestamo.fechaDevolucion = date.today()
        prestamo.save()
        # Actualizar la disponibilidad del libro
        libro_prestado.disponibilidad = 'disponible'
        libro_prestado.save()
        return redirect('detalle', pk=pk)


class ReservarLibro(View):
    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        return render(request, 'reservar_libro.html', {'libro': libro})

    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        libro.disponibilidad = 'prestado'
        libro.save()
        Prestamo.objects.create(
            libroPrestado=libro,
            fechaPrestamo=date.today(),
            usuario=request.user,
            estado='prestado')
        return render(request, 'detalle.html', {'libro': libro})


class CrearLibro(CreateView):
    model = Libro
    template_name = 'anadir_libro.html'
    fields = ['titulo', 'autores', 'editorial', 'rating', 'fechaPublicacion',
              'genero', 'isbn', 'resumen', 'disponibilidad', 'portada']
    success_url = reverse_lazy('lista_libros')


class DetallesLibro(DetailView):
    model = Libro
    template_name = 'detalle.html'


class ActualizarLibro(UpdateView):
    model = Libro
    template_name = 'editar_libro.html'
    fields = ['titulo', 'autores', 'editorial', 'rating', 'fechaPublicacion',
              'genero', 'isbn', 'resumen', 'disponibilidad', 'portada']
    success_url = reverse_lazy('lista_libros')


class BorrarLibro(DeleteView):
    model = Libro
    template_name = 'borrar_libro.html'
    success_url = reverse_lazy('lista_libros')

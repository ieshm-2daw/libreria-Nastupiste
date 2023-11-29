from typing import Any
from django.shortcuts import render, redirect
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

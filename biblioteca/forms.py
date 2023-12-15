from django import forms
from .models import *


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autores', 'editorial', 'bestSeller', 'rating', 'fechaPublicacion',
                  'genero', 'isbn', 'resumen', 'disponibilidad', 'portada']
        

class FiltroGeneroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields = ['genero']

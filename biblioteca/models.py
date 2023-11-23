from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

"""
1. Usuario: Esta clase debe extender AbstractUser de Django e incluir los campos adicionales como dni, dirección y teléfono.
"""


class Usuario(AbstractUser, models.Model):
    dni = models.CharField()
    direccion = models.CharField()
    telefono = models.PositiveBigIntegerField()

    def __str__(self):
        return self.dni


"""
3. Autor: Modelo que contiene a los autores con los campos: nombre biografía y foto.
"""


class Autor(models.Model):
    nombre = models.CharField(max_length=150).primary_key
    biografia = models.TextField()
    foto = models.ImageField()

    def __str__(self):
        return self.nombre


"""
4. Editorial: con los campos nombre, dirección y sitio web.
"""


class Editorial(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250)
    sitioWeb = models.URLField()

    def __str__(self):
        return self.nombre


"""
2. Libro: Un modelo que represente los libros de la biblioteca. Debe tener campos como título, autor(es),
editorial, fecha de publicación, género, ISBN, resumen, disponibilidad (posibles valores: disponible, prestado, 
en proceso de préstamo), portada, etc.
"""


class Libro(models.Model):
    titulo = models.CharField(max_length=150).primary_key
    autores = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    fechaPublicacion = models.DateField()
    genero = models.CharField(max_length=100)
    isbn = models.IntegerField(validators=[MinValueValidator(
        1000000000000), MaxValueValidator(9999999999999)])
    resumen = models.TextField()
    disponibilidad = models.CharField(
        choices=["Disponible", "Prestado", "En Proceso de Préstamo"])
    portada = models.ImageField()

    def __str__(self):
        return self.titulo


"""
5. Préstamo: Un modelo para registrar los préstamos de libros a los usuarios. Debe contener campos para el 
libro prestado, la fecha de préstamo, la fecha de devolución, el usuario que lo prestó y el estado del préstamo 
(prestado, devuelto).
"""


class Prestamo(models.Model):
    libroPrestado = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fechaPrestamo = models.DateField()
    fechaDevolucion = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.CharField(choices=['Prestado', 'Devuelto'])

    def __str__(self):
        return self.estado

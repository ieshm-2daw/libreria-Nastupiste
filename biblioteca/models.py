from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
"""

1. Usuario: Esta clase debe extender AbstractUser de Django e incluir los campos adicionales como dni, dirección,
 y teléfono.
"""


class Usuario(AbstractUser, models.Model):
    dni = models.CharField()
    direccion = models.CharField()
    telefono = models.PositiveBigIntegerField()

    def __str__(self):
        return self.dni


"""
2. Libro: Un modelo que represente los libros de la biblioteca. Debe tener campos como título, autor(es),
editorial, fecha de publicación, género, ISBN, resumen, disponibilidad (posibles valores: disponible, prestado, 
en proceso de préstamo), portada, etc.
"""


class Libro(models.Model):
    titulo = models.CharField(max_length=150).primary_key
    autores = models.ForeignKey()


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
5. Préstamo: Un modelo para registrar los préstamos de libros a los usuarios. Debe contener campos para el 
libro prestado, la fecha de préstamo, la fecha de devolución, el usuario que lo prestó y el estado del préstamo 
(prestado, devuelto).
"""

class Prestamo(models.Model):
    libroPrestado=models.ForeignKey(Libro,on_delete=)
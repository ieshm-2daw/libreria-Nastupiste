from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Model, CASCADE


# Create your models here.

"""
1. Usuario: Esta clase debe extender AbstractUser de Django e incluir los campos adicionales como dni, dirección y teléfono.
"""


class Usuario(AbstractUser):
    dni = models.CharField(max_length=10, unique=False)
    direccion = models.CharField(max_length=200)
    telefono = models.PositiveBigIntegerField(null=True)

    def __str__(self):
        return self.username


"""
3. Autor: Modelo que contiene a los autores con los campos: nombre biografía y foto.
"""


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    foto = models.ImageField(upload_to='autores/', null=True, blank=True)

    def __str__(self):
        return self.nombre


"""
4. Editorial: con los campos nombre, dirección y sitio web.
"""


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    sitioWeb = models.URLField()

    def __str__(self):
        return self.nombre


"""
2. Libro: Un modelo que represente los libros de la biblioteca. Debe tener campos como título, autor(es),
editorial, fecha de publicación, género, ISBN, resumen, disponibilidad (posibles valores: disponible, prestado, 
en proceso de préstamo), portada, etc.
"""


class Genero(models.Model):
    categoria = models.CharField(max_length=150)

    def __str__(self):
        return self.categoria


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    bestSeller = models.BooleanField(default=False)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    fechaPublicacion = models.DateField()
    genero = models.ManyToManyField(Genero)
    isbn = models.IntegerField(validators=[MinValueValidator(
        1000000000000), MaxValueValidator(9999999999999)])
    resumen = models.TextField()
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)

    DISPONIBILIDAD = (
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
        ('en_proceso', 'En Proceso de Préstamo'),
    )

    disponibilidad = models.CharField(max_length=20, choices=DISPONIBILIDAD)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    fechaDevolucion = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    ESTADO = ((('prestado', 'Prestado'), ('devuelto', 'Devuelto')))

    estado = models.CharField(
        max_length=20, choices=ESTADO, default='prestado')

    def __str__(self):
        return f"Préstamo de {self.libroPrestado} a {self.usuario}"

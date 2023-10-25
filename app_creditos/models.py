from typing import Any
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User

# Create your models here.

class Destino(models.Model):
    nombre = models.CharField(max_length=25, unique=True, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, default=1)

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"
        ordering = ["nombre"]

    def __str__(self):
        return f'{self.nombre}'


class Linea(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Línea')
    activa = models.BooleanField(default=False)
    destino = models.ForeignKey(Destino, on_delete=models.PROTECT)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    plazo = models.PositiveSmallIntegerField(default=2,   
        validators=[
            MinValueValidator(1),  # Rango mínimo deseado
            MaxValueValidator(4)  # Rango máximo deseado
        ]
    )
    
    tna = models.DecimalField(max_digits=8, decimal_places=2)
    tem = models.DecimalField(max_digits=8, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = "Línea"
        verbose_name_plural = "Línea"
        ordering = ["nombre"]

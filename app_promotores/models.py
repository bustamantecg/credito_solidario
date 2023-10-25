from datetime import timezone
from functools import cached_property
from django.db import models
from django.contrib.auth import get_user_model


Usuario = get_user_model()

from app_general.models import Departamento, Municipio, Provincia, Usuario

class Zona(models.Model):
    nombre = models.CharField(max_length=60, unique=True, verbose_name="Zona")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=1)         

    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zonas"
        ordering = ["nombre"]

    def __str__(self):
        return f'{self.nombre}'
    
    
# Create your models here.
class Promotor(models.Model):
    apellido = models.CharField(max_length=35, verbose_name='Apellidos')
    nombre = models.CharField(max_length=35, verbose_name='Nombres')
    cuil = models.CharField(max_length=11, verbose_name='CUIL', help_text="Sin guiones", unique=True)
    fecha_nacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    email = models.EmailField(max_length=254, help_text="Correo Electrónico", unique=True)
    domicilio = models.CharField(max_length=80)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    dpto = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='Departamento')
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    cp = models.CharField(max_length=10, verbose_name="Código Postal", help_text="Ejemplo 4700")
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)     

    class Meta:
        verbose_name = "Promotor"
        verbose_name_plural = "Promotores"
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f'{self.apellido}, {self.nombre} {self.cuil}'
    
    def documento(self):
        return f'{self.tipodoc} {self.numero}'

    @cached_property
    def edad(self):
        edad = 0
        if self.fecha_nacimiento:
            dias_anual = 365.2425
            edad = int((timezone.now().date() - self.fecha_nacimiento).days / dias_anual)
        return edad

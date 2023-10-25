from django.db import models
from django.contrib.auth import get_user_model
from app_general.models import Persona, Provincia, Departamento, Municipio
from app_promotores.models import Promotor
from ckeditor.fields import RichTextField
from django.utils.timezone import now



Usuario = get_user_model()

# Create your models here.

class Emprendimiento(models.Model):
    nombre = models.CharField(max_length=80, verbose_name='Emprendimiento')
    inicio = models.DateField(verbose_name='Inicio Actividad')
    descripcion = RichTextField(verbose_name='Descripción')
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=80)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    dpto = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='Departamento')
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    cp = models.CharField(max_length=10, verbose_name="Código Postal", help_text="Ejemplo 4700")

    referente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    promotor = models.ForeignKey(Promotor, on_delete=models.PROTECT)    
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=1)     
    
    class Meta:
        verbose_name = "Emprendimiento"
        verbose_name_plural = "Emprendimientos"
        ordering = ["nombre"]

    def __str__(self):
        return f'{self.id} - {self.nombre}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = now()
        self.updated = now()
        super(Emprendimiento, self).save(*args, **kwargs)


class Emprendedor(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    emprendimiento = models.ForeignKey(Emprendimiento, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=1)         

    class Meta:
        verbose_name = "Emprendedor"
        verbose_name_plural = "Emprendedores"
        ordering = ["-created"]

    def __str__(self):
        return f'{self.emprendimiento}'
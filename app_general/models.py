from django.db import models
from django.utils.functional import cached_property
from django.utils import timezone

from django.contrib.auth import get_user_model

# Create your models here.

Usuario = get_user_model()

class Provincia(models.Model):
    nombre = models.CharField(max_length=60, verbose_name="provincia", unique=True)
    ecodigo = models.IntegerField(null=True, blank=True)
    cdesred = models.CharField(max_length=5, null=True, blank=True)
    cvalor = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    nombre = models.CharField(max_length=60, verbose_name="departamento")
    latitud = models.CharField(max_length=20, null=True, blank=True)
    longitud = models.CharField(max_length=20, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    categoria = models.CharField(max_length=25, verbose_name="categoría", default="-")

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
    
    
class Municipio(models.Model):
    nombre = models.CharField(max_length=60, verbose_name="municipio")
    dpto = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    latitud = models.CharField(max_length=20, null=True, blank=True)
    longitud = models.CharField(max_length=20, null=True, blank=True)
    categoria = models.CharField(max_length=30, verbose_name="categoría", default="-")

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Estado Civil', help_text="help_text")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estado Civiles"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Parentesco(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Parentesco', help_text="Ejemplo Hijo/a", unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Parentesco"
        verbose_name_plural = "Parentescos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class TipoDocumento(models.Model):
    documento = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Tipo Documento"
        verbose_name_plural = "Tipos de Documentos"
        ordering = ["documento"]

    def __str__(self):
        return self.documento

class Sexo(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Sexo')

    def __str__(self):
        return self.nombre
    

class Educacion(models.Model):
    nombre = models.CharField(max_length=25, unique=True, verbose_name='Nivel Educación')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=1)     

    class Meta:
        verbose_name = "Nivel Educación"
        verbose_name_plural = "Niveles de Educación"
        ordering = ["nombre"]
    
    def __str__(self):
        return self.nombre


class Vivienda(models.Model):
    nombre = models.CharField(max_length=25, unique=True, verbose_name='Vivienda')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=1)    

    class Meta:
        verbose_name = "Vivienda"
        verbose_name_plural = "Viviendas"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Rubro(models.Model):  ## rubro economico al que se dedica la persona
    nombre = models.CharField(max_length=25, unique=True, verbose_name='Rubro Económico')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=1)   

    class Meta:
        verbose_name = "Rubro Económico"
        verbose_name_plural = "Rubros Económico"

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    apellido = models.CharField(max_length=35, verbose_name='Apellidos')
    nombre = models.CharField(max_length=35, verbose_name='Nombres')
    tipodoc = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    numero = models.CharField(max_length=12, verbose_name='Número', help_text="Sin puntos", unique=True, default=0)
    cuil = models.CharField(max_length=11, verbose_name='CUIL', help_text="Sin guiones", unique=True)
    
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.PROTECT, verbose_name='Estado Civil')    
    sexo = models.ForeignKey(Sexo, on_delete = models.PROTECT, default="Masculino")    
    vive = models.BooleanField(default=True)    
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    email = models.EmailField(max_length=254, help_text="Correo Electrónico", unique=True)
    educacion = models.ForeignKey(Educacion, on_delete = models.PROTECT)
    vivienda = models.ForeignKey(Vivienda,on_delete = models.PROTECT)
    rubro = models.ForeignKey(Rubro, on_delete = models.PROTECT, verbose_name='Rubro Económico')
    domicilio = models.CharField(max_length=80)
    provincia = models.ForeignKey(Provincia, on_delete = models.PROTECT, default='Catamarca')
    dpto = models.ForeignKey(Departamento, on_delete = models.PROTECT, verbose_name='Departamento', default='Capital')
    municipio = models.ForeignKey(Municipio, on_delete = models.PROTECT, default='Capital')
    cp = models.CharField(max_length=10, verbose_name="Código Postal", help_text="Ejemplo 4700")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)     

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
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


class Autoridad(models.Model):
    jerarquia = models.PositiveSmallIntegerField(verbose_name='gerarquia', help_text='Ejemplo 1 Mayor jerarquia ')
    cargo = models.CharField(max_length=100)
    membresia = models.CharField(max_length=10, blank=True, null=True, verbose_name='Titulo de membresia', help_text='Ejemplo Dra. C.P.N.')
    apellido = models.CharField(max_length=35, verbose_name='Apellidos')
    nombre = models.CharField(max_length=35, verbose_name='Nombres')
    imagen = models.ImageField(upload_to='autoridades', default = 'autoridades/avatar_null.jpg')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)     

    class Meta:
        verbose_name = "Autoridad"
        verbose_name_plural = "Autoridades"
        ordering = ["jerarquia"]

    def __str__(self):
        return f'{self.cargo} - {self.membresia} {self.apellido}, {self.nombre}'        
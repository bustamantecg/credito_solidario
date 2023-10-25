from django.contrib import admin

from app_general.models import *
#Persona, EstadoCivil, Provincia, Departamento, Municipio, TipoDocumento, Sexo

# Register your models here.

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "ecodigo", "cvalor")
    search_fields = ("ecodigo", "nombre", 'categoria')


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "categoria", "provincia_id", "provincia")
    list_filter = ("provincia_id", 'categoria')
    search_fields = ("provincia_id", "nombre", 'categoria')

    @admin.display(ordering='nombre', description='provincia')
    def provincia(self, obj):
        return obj.profile.provincia


class MunicipioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "categoria", 'dpto')
    list_filter = ("dpto", 'categoria')
    search_fields = ("provincia_id", "nombre", 'categoria')

    @admin.display(ordering='nombre', description='provincia')
    def provincia(self, obj):
        return obj.profile.provincia

class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    readonly_fields = ('created', 'updated')


class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ("id", "documento")


class SexoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")


class RubroAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")

class ViviendaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")

class EducacionAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'cuil', 'documento')
    readonly_fields = ('created', 'updated')
    list_filter = ("cp", 'updated', 'dpto', 'vive')
    search_fields = ('cuil', "apellido", "cp", 'updated')
    date_hierarchy = 'fecha_nacimiento'

class AutoridadAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'membresia', 'apellido', 'nombre',  'jerarquia', 'imagen')
    readonly_fields = ('created', 'updated')


admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(EstadoCivil, EstadoCivilAdmin)
admin.site.register(Sexo, SexoAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Rubro, RubroAdmin)
admin.site.register(Vivienda, ViviendaAdmin)
admin.site.register(Educacion, EducacionAdmin)
admin.site.register(Autoridad, AutoridadAdmin)


from django.contrib import admin

from app_creditos.models import Linea, Destino

# Register your models here.

class DestinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')


class LineaAdmin(admin.ModelAdmin):
    list_display = ('id', 'activa', 'nombre', 'destino', 'tna', 'tem', 'importe', 'plazo')
    readonly_fields = ('created', 'updated')
    list_filter = ('activa', 'destino')
    search_fields = ('id', 'nombre', 'destino')


admin.site.register(Linea, LineaAdmin)
admin.site.register(Destino, DestinoAdmin)

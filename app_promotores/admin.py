from django.contrib import admin

from app_promotores.models import Zona, Promotor
# Register your models here.

class ZonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'created', 'updated')
    readonly_fields = ('created', 'updated')    
    search_fields = ('id', 'nombre')

class PromotorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'cuil' )
    readonly_fields = ('created', 'updated')
    list_filter = ("cp", 'updated', 'dpto')
    search_fields = ('cuil', "apellido", "cp", 'updated')    


admin.site.register(Zona, ZonaAdmin)
admin.site.register(Promotor, PromotorAdmin)
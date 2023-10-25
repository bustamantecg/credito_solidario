from django.contrib import admin

from app_emprendimientos.models import Emprendimiento, Emprendedor

# Register your models here.

class EmprendedorAdmin(admin.ModelAdmin):
    list_display = ('persona',)
    readonly_fields = ('created', 'updated')
    #list_filter = ("cp", 'updated', 'dpto')
    #search_fields = ('nombre', 'referente', 'created')    
    
class InstanciaEmprendedor(admin.TabularInline):
    model = Emprendedor

class EmprendimientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'referente', 'created')
    inlines =[InstanciaEmprendedor]
    readonly_fields = ('created', 'updated')
    list_filter = ("cp", 'updated', 'dpto')
    search_fields = ('nombre', 'referente', 'created')    

admin.site.register(Emprendimiento, EmprendimientoAdmin)
admin.site.register(Emprendedor, EmprendedorAdmin)
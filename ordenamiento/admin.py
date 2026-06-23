from django.contrib import admin
from .models import Barrio, Parroquia, PresidenteBarrio


class ParroquiaAdmin(admin.ModelAdmin):
        list_display = ('nombre', 'ubicacion', 'tipo')
        search_fields = ('nombre',)
        list_filter = ('ubicacion', 'tipo') 
admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):
        list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia')
        search_fields = ('nombre',)
        list_filter = ('parroquia',)
admin.site.register(Barrio, BarrioAdmin)


class PresidenteBarrioAdmin(admin.ModelAdmin):
        list_display = ('cedula', 'nickname', 'edad', 'profesion', 'barrio')
        search_fields = ('cedula', 'nickname')
        list_filter = ('barrio',)
admin.site.register(PresidenteBarrio, PresidenteBarrioAdmin)
# Register your models here.

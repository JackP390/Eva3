from django.contrib import admin
from .models import SalaEstudio, Reserva

class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'disponible', 'en_mantenimiento')
    list_filter = ('disponible', 'en_mantenimiento')
    search_fields = ('nombre',)
    list_editable = ('disponible', 'en_mantenimiento')
    list_per_page = 10

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('sala_reservada', 'rut_reservante', 'hora_inicio', 'hora_termino')
    list_filter = ('sala_reservada', 'hora_inicio')
    search_fields = ('rut_reservante',)

# Register your models here.
admin.site.register(SalaEstudio, SalaAdmin)
admin.site.register(Reserva, ReservaAdmin)
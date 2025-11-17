from django.contrib import admin
from .models import SalaEstudio
from .models import Reserva

# Register your models here.
admin.site.register(SalaEstudio)
admin.site.register(Reserva)
from django.db import models

# Create your models here.
class SalaEstudio(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    en_mantenimiento = models.BooleanField(default=False)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    rut_reservante = models.CharField(max_length=12)
    sala_reservada = models.ForeignKey(SalaEstudio, on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField(auto_now_add=True)
    hora_termino = models.DateTimeField()

    def __str__(self):
        return f"Reserva de la sala {self.sala_reservada.nombre} por RUT: {self.rut_reservante}"
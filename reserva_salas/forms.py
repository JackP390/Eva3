from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['rut_reservante']
        widgets = {'rut_reservante':forms.TextInput(attrs={'class':'form-control', 'placeholder':'12345678-9'})}
        labels = {'rut_reservante':'Ingresa tu RUT para confirmar'}
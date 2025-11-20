from django import forms
from django.core.exceptions import ValidationError
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['rut_reservante']
        widgets = {'rut_reservante':forms.TextInput(attrs={'class':'form-control', 'placeholder':'12345678-9'})}
        labels = {'rut_reservante':'Ingresa tu RUT para confirmar'}

    def clean_rut_reservante(self):
        rut = self.cleaned_data.get('rut_reservante')

        rut = rut.replace('.', '')

        if '-' not in rut:
            raise ValidationError("El RUT debe incluir el guion (Ej: 11111111-1)")
        
        partes = rut.split('-')

        if len(partes) != 2:
            raise forms.ValidationError("Error de RUT inválido.")
        
        cuerpo = partes[0]
        dv = partes[1]

        if not cuerpo.isdigit():
            raise forms.ValidationError("La parte antes del guión debe contener solo números")
        
        if not dv.isdigit() and dv.upper() != 'K':
            raise forms.ValidationError("El dígito verificador debe ser un número o la letra K.")
        
        if len(cuerpo) < 7:
            raise forms.ValidationError("El RUT es demasiado corto.")
        
        return rut
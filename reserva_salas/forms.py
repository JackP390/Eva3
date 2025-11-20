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
        
        if len(rut) < 8:
            raise ValidationError("El RUT parece demasiado corto.")
        
        cuerpo, dv = rut.split('-')
        if len(dv) != 1:
            raise ValidationError("El dígito verificador debe ser un solo caracter.")
        
        return rut
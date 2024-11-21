from django import forms
from .models import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre','dni','direccion','correo','nombrelibro','categoria','cantidadDias','celular']
        widgets = {'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido y Nombre'}),
                   'dni': forms.TextInput(attrs={'class':'form-control','placeholder':'DNI'}),
                   'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion'}),
                   'correo': forms.TextInput(attrs={'class':'form-control','placeholder':'Correo'}),
                   'nombrelibro': forms.TextInput(attrs={'class':'form-control','placeholder':'Libro'}),
                    'categoria': forms.TextInput(attrs={'class':'form-control','placeholder':'Categoria'}),
                    'cantidadDias': forms.TextInput(attrs={'class':'form-control','placeholder':'Tiempo de prestamo'}),
                    'celular': forms.TextInput(attrs={'class':'form-control','placeholder':'Celular'}),
                   }
        labels = {'nombre':'', 'dni':'', 'direccion':'', 'correo':'', 'nombrelibro':'', 'categoria':'', 'cantidadDias':'', 'celular':''}

""" class Fechas(forms.Form):
    fechaInicio = forms.DateField(
        label="Fecha de prestamo",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )
    vencimiento = forms.DateField(
        label="Fecha de vencimiento",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    ) """

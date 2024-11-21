from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo','autor','isbn','categoria','estado','numInvent','imagen']
        widgets = {'titulo': forms.TextInput(attrs={'class':'form-control','placeholder':'Título'}),
                   'autor': forms.TextInput(attrs={'class':'form-control','placeholder':'Autor'}),
                   'isbn': forms.TextInput(attrs={'class':'form-control','placeholder':'ISBN'}),
                   'categoria': forms.TextInput(attrs={'class':'form-control','placeholder':'Categoría'}),
                   'estado': forms.TextInput(attrs={'class':'form-control','placeholder':'Estado'}),
                   'numInvent': forms.TextInput(attrs={'class':'form-control','placeholder':'Número de Inventario'}),

                   }
        labels = {'titulo':'', 'autor':'', 'isbn':'', 'categoria':'', 'estado':'', 'numInvent':'', 'imagen':''}
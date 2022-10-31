from django import forms
from django import forms

from .models import Producto

class ProductAddForm(forms.ModelForm):
    class Meta:
        model=Producto
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input-form'}),
        }
        fields=('nombre','categoria','precio')
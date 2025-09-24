from django import forms
from .models import Movimiento
from producto.models import Producto
from bodega.models import Bodega

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ['producto', 'bodega', 'tipo', 'cantidad', 'observacion']
        widgets = {
            
            'observacion': forms.Textarea(attrs={'rows': 2}),
        }

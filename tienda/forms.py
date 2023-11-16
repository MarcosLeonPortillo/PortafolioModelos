from django import forms
from .models import Producto

class editarProducto(request):
    vip = forms.BooleanField(label='vip', initial=False)
    columnas = forms.IntegerField(label='Columnas', min_value=1, max_value=15, required=True, initial=2)
    nMinas = forms.IntegerField(label='Minas', min_value=1, required=True, initial=2)

        def clean(self):
            cleaned_data = super().clean()
            filas = cleaned_data.get("filas")
            columnas = cleaned_data.get("columnas")
            nMinas = cleaned_data.get("nMinas")

            if nMinas > (columnas * filas) / 2:
                r
                aise ValidationError("El valor de minas no es válido")

            return cleaned_data
        
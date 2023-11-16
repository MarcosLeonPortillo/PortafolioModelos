from django import forms
from django.core.exceptions import ValidationError
class TableroForm(forms.Form):
    filas = forms.IntegerField(label='Filas', min_value=1, max_value=20, required=True, initial=2)
    columnas = forms.IntegerField(label='Columnas', min_value=1, max_value=15, required=True, initial=2)
    num_minas = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        filas = cleaned_data.get('filas')
        columnas = cleaned_data.get('columnas')
        num_minas = cleaned_data.get('num_minas')

        if num_minas:
            if num_minas < 0:
                raise ValidationError("El valor de minas no puede ser menor que 0")

            if num_minas > (filas * columnas) / 2:
                raise ValidationError("El valor de minas no puede ser mayor que la mitad de la multiplicacion de columnas y filas")

        return cleaned_data

from django import forms
from .models import * # Importar todos los objetos

class TVForma(forms.ModelForm):
    class Meta:
        model = Televisores
        fields = ['descripcion', 'marca', 'modelo', "resolucion"]

class CelularForma(forms.ModelForm):
    class Meta:
        model = TelefonoCelular
        fields = ['descripcion', 'marca', 'modelo', "procesador"]
        
class LaptopForma(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['descripcion', 'marca', 'modelo', "procesador", "tamano_pantalla"]

        
class TVDeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(
        required=True,
        initial=False,
        widget=forms.HiddenInput,
    )
from django import forms
from .models import Televisores

class TVForma(forms.ModelForm):
    class Meta:
        model = Televisores
        fields = ['descripcion', 'marca', 'modelo', "resolucion"]
        
class TVDeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(
        required=True,
        initial=False,
        widget=forms.HiddenInput,
    )
from django import forms
from django.forms import DateInput
from ..models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['nome', 'nascimento', 'categoria', 'cor']
        exclude = ['dono']
        widgets = {
            'nascimento': DateInput(attrs={'type': 'date'})
        }
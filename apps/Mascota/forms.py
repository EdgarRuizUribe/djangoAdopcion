from django import forms
from apps.Mascota.models import Pet

class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = [
            'name',
            'sex',
            'aproximated_ege',
            'rescue_date',
            'persons',
        ]

        labels = {
            'name':'Nombre',
            'sex':'Sexo',
            'aproximated_ege':'Edad',
            'rescue_date':'Fecha de rescate',
            'persons':'Adoptado por',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-name form-control'}),
            'sex': forms.Select(attrs={'class':'form-sex form-control'}),
            'aproximated_ege': forms.TextInput(attrs={'class':'form-name form-control'}),
            'rescue_date': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'persons': forms.Select(attrs={'class':'form-name form-control'}),
        }
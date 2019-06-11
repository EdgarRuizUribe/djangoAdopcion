from django import forms
from apps.adopcion.models import Person, Telephone

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = [
            'name',
            'last_name',
            'age',
            'email',
        ]

        labels = {
            'name':'Nombre',
            'last_name':'Apellido',
            'age': 'Edad',
            'email': 'Email',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'persona-name'}),
            'last_name': forms.TextInput(attrs={'class':'last-name'}),
            'age': forms.NumberInput(attrs={'class':'edad'}),
            'Email': forms.EmailInput(attrs={'class': 'email'}),
        }


class TelephoneForm(forms.ModelForm):

    class Meta:
        model = Telephone
        fields = [
            'sort',
            'number',
        ]

        labels = {
            'sort':'Tipo',
            'number':'Numero',
        }

        widgets = {
            'sort':forms.Select(),
            'number':forms.TextInput(attrs={'class':'numero-telefono'}),
        }
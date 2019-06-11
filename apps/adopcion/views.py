from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

# Create your views here.

from apps.adopcion.models import Person
from apps.adopcion.forms import PersonForm, TelephoneForm

class PersonList(ListView):
    model = Person
    template_name = 'listar_personas.html'

class PersonDetail(DetailView):
    model = Person
    template_name = 'detail_persona.html'


class PersonaDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('personas_listar')


class PersonaUpdate(UpdateView):
    model = Person
    form = PersonForm
    form_two = TelephoneForm

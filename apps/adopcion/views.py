from django.shortcuts import render

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

# Create your views here.

from apps.adopcion.models import Person, Telephone
from apps.adopcion.forms import PersonForm, TelephoneForm

class PersonList(ListView):
    model = Person
    template_name = 'listar_personas.html'


class PersonDetail(DetailView):
    model = Person
    template_name = 'detail_persona.html'


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('personas_listar')


class PersonCreate(CreateView):
    model = Telephone
    template_name = 'crear_persona.html'
    form_class = TelephoneForm
    second_form_class = PersonForm
    success_url = reverse_lazy('personas_listar')

    def get_context_data(self, **kwargs):
        context = super(PersonCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.second_form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            thelephone = form.save(commit=False)
            thelephone.Persons = form2.save()
            thelephone.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class PersonUpdate(UpdateView):
    model = Telephone
    second_model = Person
    template_name = 'actualizar_persona.html'
    form_class = TelephoneForm
    second_form_class = PersonForm

    def get_context_data(self, **kwargs):
        context = super(PersonUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        persona = self.second_model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona) 
        context['id'] = pk
        return context

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object
    

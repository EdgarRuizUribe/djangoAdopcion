from django.shortcuts import render

from django.db import transaction
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

# Create your views here.

from apps.adopcion.models import Person, Telephone
from apps.adopcion.forms import PersonForm, TelephoneForm, TelephoneFormSet

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
    model = Person
    template_name = 'crear_persona.html'
    form_class = PersonForm
    telephoneFormSet = TelephoneFormSet
    success_url = reverse_lazy('personas_listar')

    def get_context_data(self, **kwargs):
        context = super(PersonCreate, self).get_context_data(**kwargs)
        # if 'form' not in context:
        #     context['form'] = self.form_class()
        # if 'form2' not in context:
        #     context['form2'] = self.telephoneFormSet()
        # return context
        if self.request.POST:
            context['form2'] = TelephoneFormSet(self.request.POST)
        else:
            context['form2'] = TelephoneFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form2 = context['form2']
        with transaction.atomic():
            self.object = form.save()

            if form2.is_valid():
                form2.instance = self.object
                form2.save()

        messages.success(self.request, 'Registro con éxito')
        return super(PersonCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Verifica la información')
        return super(PersonCreate, self).form_invalid(form)


# En este codigo se sobre escribe el metodo PSOT  y guardo en un click 2 forms dostintos, lugados por un foreign key
# la variable form_clas y second_form_class. tienen que llamarce forsosamente así
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object
    #     form = self.form_class(request.POST)
    #     form2 = self.second_form_class(request.POST)
    #     if form.is_valid() and form2.is_valid():
    #         thelephone = form.save(commit=False)
    #         thelephone.Persons = form2.save()
    #         thelephone.save()
    #         return HttpResponseRedirect(self.get_success_url())
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form, form2=form2))


class PersonUpdate(UpdateView):
    model = Person
    template_name = 'actualizar_persona.html'
    form_class = PersonForm
    telephoneFormSet = TelephoneFormSet
    success_url = reverse_lazy('personas_listar')

    def get_context_data(self, **kwargs):
        data = super(PersonUpdate, self).get_context_data(**kwargs)

        if self.request.POST:
            data['form2'] = TelephoneFormSet(self.request.POST, instance=self.object)
        else:
            data['form2'] = TelephoneFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        form2 = context['form2']
        with transaction.atomic():
            self.object = form.save()
            if form2.is_valid():
                form2.instance = self.object
                form2.save()

        messages.success(self.request, 'Registro con éxito')
        return super(PersonUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Verifica la información')
        return super(PersonUpdate, self).form_invalid(form)
    

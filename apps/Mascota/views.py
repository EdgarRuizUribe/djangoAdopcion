from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from apps.Mascota.models import Pet

from apps.Mascota.forms import PetForm

# Create your views here.

class MascotasList(ListView):
    model = Pet
    template_name = 'list_mascotas.html'

class MascotaDetail(DetailView):
    model = Pet
    template_name = 'detail_mascota.html'
    
    # def get_object(self):
    #     pk_ = self.kwargs.get('pk')
    #     return get_object_or_404(Pet, pk=pk_)


class MascotaUpdate(UpdateView):
    model=Pet
    form_class = PetForm
    template_name = 'actualizar_mascota.html'
    success_url= reverse_lazy('mascotas_listar')


class MascotaCreate(CreateView):
    model=Pet
    form_class = PetForm
    template_name = 'crear_mascota.html'
    success_url= reverse_lazy('mascotas_listar')


class MascotaDelete(DeleteView):
    model = Pet
    template_name = 'delete_mascota.html'
    success_url= reverse_lazy('mascotas_listar')


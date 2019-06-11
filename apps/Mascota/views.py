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

# Para el proceso de eliminacion.
# DeleteView utiliza el atributo template_name cuando la peticion es un get. esto para confirmar en un html la eliminacion.

# se lo que se quiere es no utilizar un html de confirmacion, se tiene que resivir un POST y solo dirijir al success_url.

# para enviar un post desde un form html se utiliza los atributos actiom="nombre de la view para el delete" y method="POST"
class MascotaDelete(DeleteView):
    model = Pet
    # template_name = 'delete_mascota.html'
    success_url= reverse_lazy('mascotas_listar')


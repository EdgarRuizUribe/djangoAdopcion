"""formulario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from apps.Mascota.views import MascotasList, MascotaDetail, MascotaDelete, MascotaUpdate, MascotaCreate

urlpatterns = [
    path('', MascotasList.as_view(), name='mascotas_listar'),
    path('detalle/<int:pk>/', MascotaDetail.as_view(), name='mascota_detalle'),
    path('eliminar/<int:pk>/', MascotaDelete.as_view(), name='mascota_eliminar'),
    path('actializar/<int:pk>/', MascotaUpdate.as_view(), name='mascota_actualizar'),
    path('nuevo/', MascotaCreate.as_view(), name='mascota_crear'),
]
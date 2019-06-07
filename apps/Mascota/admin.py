from django.contrib import admin
from apps.Mascota.models import Pet
from apps.adopcion.models import Person, Telephone

# Register your models here.


admin.site.register(Pet)
admin.site.register(Person)
admin.site.register(Telephone)
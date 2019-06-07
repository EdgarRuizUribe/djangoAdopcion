from django.db import models
from  apps.adopcion.models import Person

# Create your models here.
SEX_CHOICES = (
    ('', 'Selecciona un sexo'),
    ('M', 'Macho'),
    ('H', 'Hembra')
)


class Pet(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default=None)
    aproximated_ege= models.IntegerField()
    rescue_date = models.DateField()
    persons = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.name)
    
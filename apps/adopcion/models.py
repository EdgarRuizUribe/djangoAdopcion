from django.db import models

# Create your models here.

SORT_CHOICES = (
    ('', 'Selecciona tipo de Telefono'),
    ('Fijo','CASA'),
    ('Movil', 'CELULAR'),
)
    

class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.name, self.last_name)


class Telephone(models.Model):
    Persons = models.ForeignKey(Person,null=True, blank=True, on_delete=models.CASCADE)
    sort = models.CharField(max_length=6, choices=SORT_CHOICES, default=None)
    number = models.CharField(max_length=12)

    def __str__(self):
        return "{}".format(self.number)
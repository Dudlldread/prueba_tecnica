from msilib.schema import Class
from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(null=False,max_length=255)
    apellido = models.CharField(null=True,max_length=255)
    nacimiento = models.DateField(null=True)
    telefono = models.CharField(null=True,max_length=255)
    email = models.EmailField(null=False,max_length=255)

    class Meta:
        db_table = 'Cliente'

    def __str__(self):
        return self.nombre
 
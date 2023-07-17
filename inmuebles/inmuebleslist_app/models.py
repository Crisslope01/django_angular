from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=150)
    website = models.URLField(max_length=200)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    direccion = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    empresa = models.ForeignKey('Empresa', related_name='inmuebles', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.direccion
    


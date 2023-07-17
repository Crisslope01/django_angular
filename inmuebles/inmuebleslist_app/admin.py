from django.contrib import admin
from .models import Inmueble, Empresa

# Register your models here.

admin.site.register(Inmueble)
admin.site.register(Empresa)
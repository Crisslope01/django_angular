from django.shortcuts import render
from .models import Inmueble
from django.http import JsonResponse

# Create your views here.

def inmuebles_list(request):
    inmuebles = Inmueble.objects.all()
    data = {
        'inmuebles': list(inmuebles.values('direccion', 'pais', 'descripcion', 'imagen', 'active'))
    }
    return JsonResponse(data)
    

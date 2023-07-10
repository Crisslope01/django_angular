#from django.shortcuts import render
#from .models import Inmueble
#from django.http import JsonResponse

# Create your views here.

#def inmuebles_list(request):
    #inmuebles = Inmueble.objects.all()
    #data = {
        #'inmuebles': list(inmuebles.values('direccion', 'pais', 'descripcion', 'imagen', 'active'))
    #}
    #return JsonResponse(data)
    
#def inmuebles_detail(request, pk):
    #inmueble = Inmueble.objects.get(pk=pk)
    #data = {
        #'inmueble': {
            #'direccion': inmueble.direccion,
            #'pais': inmueble.pais,
            #'descripcion': inmueble.descripcion,
            #'imagen': inmueble.imagen.url,
            #'active': inmueble.active
        #}
    #}
    #return JsonResponse(data)
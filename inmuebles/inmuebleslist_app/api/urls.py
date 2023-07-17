from django.urls import path
#from inmuebleslist_app.api.views import inmuebles_list, inmuebles_detail
from . import views
from inmuebleslist_app.api.views import InmueblelistAV, InmuebleDetailAV, EmpresaAV
urlpatterns = [
    path('list/', InmueblelistAV.as_view(), name='inmuebles_list'),
    path('list/<int:pk>/', InmuebleDetailAV.as_view(), name='inmuebles_detail'),
    path('empresa/',EmpresaAV.as_view(), name='empresa'),
    
]
from django.urls import path
from inmuebleslist_app.views import inmuebles_list
from . import views


urlpatterns = [
    path('list/', views.inmuebles_list, name='inmuebles_list'),
]
from django.urls import path
from inmuebleslist_app.api.views import inmuebles_list, inmuebles_detail
from . import views

urlpatterns = [
    path('list/', views.inmuebles_list, name='inmuebles_list'),
    path('list/<int:pk>/', views.inmuebles_detail, name='inmuebles_detail')
]
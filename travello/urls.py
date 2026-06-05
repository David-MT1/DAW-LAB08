from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar, name='agregar'),
    path('modificar/<int:pk>/', views.modificar, name='modificar'),
    path('eliminar/<int:pk>/', views.eliminar, name='eliminar')
]

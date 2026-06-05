from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('suma', views.suma, name='suma')
]

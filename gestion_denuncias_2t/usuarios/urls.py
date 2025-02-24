from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='usuarios.index'),
    path('registro', views.registro, name='usuarios.registro'),
    path('login', views.iniciar_sesion, name='usuarios.login'),
    path('logout', views.cerrar_sesion, name='usuarios.logout'),
]

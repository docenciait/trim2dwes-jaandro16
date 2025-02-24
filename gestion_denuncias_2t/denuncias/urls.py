from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('denuncias', views.listar_denuncias, name='denuncias.listar_denuncias'),
    path('denuncias/crear/', views.crear_denuncia, name='denuncias.crear_denuncia'),
]

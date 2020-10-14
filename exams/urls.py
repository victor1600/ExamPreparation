from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('materias/', views.materiasList, name='get-materias'),
]

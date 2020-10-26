from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('materia-list/', views.materiasList, name='materia-list'),
    path('materia-detail/<str:pk>', views.materiaDetail, name='materia-detail'),
    path('materia-create/', views.materiaCreate, name='materia-create'),
    path('materia-update/<str:pk>', views.materiaUpdate, name='materia-update'),
    path('materia-delete/<str:pk>', views.materiaDelete, name='materia-delete'),
    path('facultad-list/', views.facultadesList, name='facultad-list'),
    path('facultad-create/', views.facultadCreate, name='facultad-create'),

]

from django.contrib import admin
from .models import Facultad, Escuela, Ciclo, Materia

# Register your models here.
admin.site.register(Facultad)
admin.site.register(Escuela)
admin.site.register(Ciclo)
admin.site.register(Materia)

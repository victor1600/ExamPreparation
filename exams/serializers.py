from rest_framework import serializers
from .models import Facultad, Escuela, Ciclo, Materia


class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        # Avoid getting the status (activo, inactivo) when fetching data
        fields = ['id', 'nombre']


class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = '__all__'


class CicloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciclo
        fields = '__all__'


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Materia, Facultad
from .serializers import MateriaSerializer, FacultadSerializer


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Materias-List': '/materias/'
    }
    return Response(api_urls)


@api_view(['GET'])
def materiasList(request):
    materias = Materia.objects.all()
    serializer = MateriaSerializer(materias, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def materiaDetail(request, pk):
    materia = Materia.objects.get(id=pk)
    serializer = MateriaSerializer(materia, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def materiaCreate(request):
    serializer = MateriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['POST'])
def materiaUpdate(request, pk):
    materia = Materia.objects.get(id=pk)
    serializer = MateriaSerializer(instance=materia, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def materiaDelete(request, pk):
    materia = Materia.objects.get(id=pk)
    materia.delete()
    return Response('Item successfully deleted!')


# views for Facultad
@api_view(['GET'])
def facultadesList(request):
    facultades = Facultad.objects.all()
    serializer = FacultadSerializer(facultades, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def facultadCreate(request):
    serializer = FacultadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

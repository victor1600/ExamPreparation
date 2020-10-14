from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Materia
from .serializers import MateriaSerializer
# Create your views here.

@api_view(['GET'])
def materiasList(request):
    materias = Materia.objects.all()
    serializer = MateriaSerializer(materias, many=True)
    return Response(serializer.data)
    #return 'hello world!'

from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.serializers import RegistrationSerializer


@api_view(['POST'])
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        # We use the overriden method
        account = serializer.save()
        data['response'] = "successfully registered a new user."
        data['email'] = account.email
        data['username'] = account.username
    else:
        data = serializer.errors
    return Response(data)

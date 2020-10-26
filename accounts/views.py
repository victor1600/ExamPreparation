from django.contrib.auth import login, authenticate
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from accounts.serializers import RegistrationSerializer


# @api_view(['POST'])
# def register(request):
#     data = request.data
#     username = data['username']
#     email = data['email']
#     password = data['password']
#     if User.objects.filter(username=username).exists():
#         return Response({'message': 'That username is taken'})
#     if User.objects.filter(email=email).exists():
#         return Response({'message': 'That email is taken'})
#
#     user = User.objects.create_user(username=username, email=email, password=password)
#     user.save()
#     # print('user saved')
#     return Response({'message': 'User saved successfully'})

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

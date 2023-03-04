from django.conf import settings
from django.shortcuts import redirect, render, resolve_url
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from django.contrib.auth.forms import AuthenticationForm

from auth.models import User
from auth.serializers import UserSerializer, RegisterSerializer


# Create your views here.

class UserViewset(ModelViewSet):
    
    serializer_class = UserSerializer
    
    
    def get_queryset(self):
        return User.objects.all()
    

@api_view(['POST',])
def RegisterView(request):
    serializer = RegisterSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = "Succes"
        data['email'] = user.email
        data['first_name'] = user.first_name
        data['last_name'] = user.last_name
        data['username'] = user.username
    else:
        data = serializer.errors
    
    return Response(data)

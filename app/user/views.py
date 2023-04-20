from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.settings import api_settings
from user.serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from user.serializers import UserSerializer, TokenSerializer


class CreateUserView(generics.CreateAPIView):
    """View to handle creating a user"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """View to create and return auth token for authenticated user"""
    serializer_class = TokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

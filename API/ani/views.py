from django.shortcuts import render
from rest_framework import viewsets
from .models import Photos, Songs
from .serializer import PhotoSerializer, SongSerializer, UserSerializer
from django.contrib.auth.models import User

class PhotoView(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

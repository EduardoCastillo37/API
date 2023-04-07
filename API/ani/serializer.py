from rest_framework import serializers
from .models import Photos, Songs
from django.contrib.auth.models import User


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photos
        fields = ('pk', 'title', 'photo')


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Songs
        fields = ('pk', 'title', 'song')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

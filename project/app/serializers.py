from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project, Client
from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__' 

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'projects']

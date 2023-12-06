from rest_framework import serializers
from .models import Algorithm
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",)

class AlgorithmSerializer(serializers.HyperlinkedModelSerializer):

    owner = UserSerializer()

    class Meta:
        model = Algorithm
        fields = ['id', 'name', 'creation_date', 'algorithm_file', 'owner']

    
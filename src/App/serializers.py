from rest_framework import serializers
from .models import TodoModel
from django.contrib.auth.models import User

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id', 'title', 'content', 'owner']
        owner = serializers.ReadOnlyField(source = 'owner.username')

class UserSerializer(serializers.ModelSerializer):
    todo = serializers.PrimaryKeyRelatedField(many=True, queryset=TodoModel.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'todo']
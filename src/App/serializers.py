from rest_framework import serializers
from .models import TodoModel

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id', 'title', 'content']

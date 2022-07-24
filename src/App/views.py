from rest_framework.views import APIView
from .models import TodoModel
from django.http import Http404
from .serializers import Serializer
from rest_framework.response import Response

class TodoCollection(APIView):
    def get(self, request, format=None):
        todo_list = TodoModel.objects.all()
        serializer = Serializer(todo_list, many=True)

        return Response(serializer.data)

class TodoSingle(APIView):
    def get_object(self, pk):
        try:
            return TodoModel.objects.get(pk=pk)
        except TodoModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo_item = self.get_object(pk)
        serializer = Serializer(todo_item)

        return Response(serializer.data)

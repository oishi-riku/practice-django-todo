from .models import TodoModel
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .serializers import Serializer

class TodoList(ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = Serializer
    permission_classes = []

class TodoListItem(RetrieveAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = Serializer
    permission_classes = []
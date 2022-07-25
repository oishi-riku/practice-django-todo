from .models import TodoModel
from .serializers import Serializer
from rest_framework import generics, filters, pagination
from django_filters.rest_framework import DjangoFilterBackend

class Pagination(pagination.LimitOffsetPagination):
    page_size = 5

# Generic View

class TodoCollection(generics.ListCreateAPIView):
    queryset = TodoModel.objects.filter()
    serializer_class = Serializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['content', '=title']

class TodoSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = Serializer

# View Set

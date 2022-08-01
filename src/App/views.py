from .models import TodoModel
from .serializers import Serializer, UserSerializer
from rest_framework import generics, filters, pagination, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly

class Pagination(pagination.LimitOffsetPagination):
    page_size = 5

class TodoCollection(generics.ListCreateAPIView):
    queryset = TodoModel.objects.filter()
    serializer_class = Serializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['content', '=title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class TodoSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserCollection(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSingle(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

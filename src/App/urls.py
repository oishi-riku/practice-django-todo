from django.urls import path
from . import apis

urlpatterns = [
    path('api/', apis.TodoList.as_view(), name = 'api'),
    path('api/<int:pk>/', apis.TodoListItem.as_view(), name = 'api_single'),
]

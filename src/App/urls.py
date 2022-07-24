from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from . import apis
from . import views

urlpatterns = [
    path('api/todo', views.TodoCollection.as_view(), name='todo_collection'),
    path('api/todo/<int:pk>', views.TodoSingle.as_view(), name='todo_single'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from . import apis
from . import views

urlpatterns = [
    path('api/todo/', views.TodoCollection.as_view()),
    path('api/todo/<int:pk>/', views.TodoSingle.as_view()),
    path('api/user', views.UserCollection.as_view()),
    path('api/user/<int:pk>', views.UserSingle.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
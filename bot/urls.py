from django.urls import path
from .views import ToDoListAPIView, MusicListView

urlpatterns = [
    path('music/', ToDoListAPIView.as_view()),
    path('filter/<name>/', MusicListView.as_view()),
]
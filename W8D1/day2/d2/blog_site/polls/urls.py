from django.urls import path
from .views import index, profile, posts

urlpatterns = [
    path('index', index, name='index'), 
    path('profile', profile, name='profile'), 
    path('posts/<int:author_id>', posts, name='posts'), 
]
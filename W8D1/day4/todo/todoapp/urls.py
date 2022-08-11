from django.contrib import admin
from django.urls import path
from .views import create_category, create_todo, display_todos, home, todo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo",todo, name="todo"),
    path('all',display_todos,name = 'all'),
    path('add',create_todo,name = 'todocreation'),
    path('category',create_category,name='category'),
    path("", home , name="home")
]
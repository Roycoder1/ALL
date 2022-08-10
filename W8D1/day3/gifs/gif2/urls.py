from unicodedata import category
from django.contrib import admin

from django.urls import path

from .views import  category_view, create_gif, get_gif, create_category
from .views import index
urlpatterns = [
    path('', get_gif , name='get_gif'),
    path('homepage',index, name= 'homepage'),
    path('forms',create_category, name= 'create_category'),
    path("create_gif", create_gif, name= 'create_gif'),
    path("category/<int:id>", category_view,name='category'),
    
]
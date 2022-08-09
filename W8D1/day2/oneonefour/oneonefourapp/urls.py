from django.contrib import admin
from django.urls import include,path
from .views import (get_by_name, get_by_number)

urlpatterns = [
    path("info/<str:name>",get_by_name,name = 'get_by_name'),
    path("info/<str:number>",get_by_number,name = 'get_by_number')

    
]
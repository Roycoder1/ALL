from django.contrib import admin
from django.urls import path

from .views import display_info,vacancies,more_info

urlpatterns = [
    path("",display_info,name="homepage"),
    path("date", vacancies , name = 'date'),
    path("info", more_info , name = 'info'),
]
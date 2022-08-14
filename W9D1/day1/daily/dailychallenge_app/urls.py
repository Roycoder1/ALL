from django.contrib import admin
from django.urls import path

from dailychallenge_app.views import daily


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", daily, name="form")
]
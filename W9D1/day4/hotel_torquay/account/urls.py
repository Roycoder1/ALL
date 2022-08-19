from django.contrib import admin
from django.urls import path, include

from account.views import profile, signup


urlpatterns = [
    path("/signup",signup, name="signup"),
    path("profile/",profile, name="profile"),
]
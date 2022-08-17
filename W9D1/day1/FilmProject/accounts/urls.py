from django.urls import path
from .views import (
    profile,
    profile_user,
    signup, 
    signin, 
    signout,
    update_profile)

urlpatterns = [
    path("signup", signup, name='signup'),
    path("signin", signin, name="signin"),
    path("signout", signout, name="signout"),
    path("update-profile", update_profile, name="update"),
    path("profile_user",profile_user, name='profile_user'),
    path("user-profile",profile, name='profile'),
]
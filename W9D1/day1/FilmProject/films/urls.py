from django.urls import path,include

from films.views import addDirector, addFilm, home

urlpatterns = [
    path("homepage",home,name= 'homepage'),
    path("addFilm", addFilm, name="addFilm"),
    path("addDirector", addDirector, name="addDirector")

]
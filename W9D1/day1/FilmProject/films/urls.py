from django.urls import path,include

from films.views import addDirector, addFilm, home, update_director, update_film

urlpatterns = [
    path("homepage",home,name= 'homepage'),
    path("addFilm", addFilm, name="addFilm"),
    path("addDirector", addDirector, name="addDirector"),
    path("update/<int:id>", update_film, name="update"),
    path("director/<int:id>", update_director, name="update-director"),
    # path("homepage",homepage.as_view(), name='homepage')

]
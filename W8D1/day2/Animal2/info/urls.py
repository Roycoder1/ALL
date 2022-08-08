from . import views
from django.urls import include, path

urlpatterns = [
    path("" , views.index ,name = 'index'),
    path("animal",views.animal,name='animal'),
    path ("animals",views.animals,name = 'animals')

]
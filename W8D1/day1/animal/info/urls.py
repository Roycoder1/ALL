from django.urls import path
from . import views


urlpatterns = [
    path('index',views.index, name = 'index'),
    # path('family/<int:id>',views.show_family,name=)


]
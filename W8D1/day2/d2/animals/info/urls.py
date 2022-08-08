from django.urls import path
from .views import show_family, show_animal, show_animals

urlpatterns = [
    path('family/<int:id>', show_family, name='show_family'),
    path('animal/<int:id>', show_animal, name='show_animal'),
    path('animals', show_animals, name='show_animals'),
]

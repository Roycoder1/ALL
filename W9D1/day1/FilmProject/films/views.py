

from re import A
from django.shortcuts import render
from .models import Director, Film
from films.forms import AddDirectorForm, AddFilmForm

# Create your views here.

def addFilm(request):
    context = {'form': AddFilmForm}
    if request.method == 'POST':

        film = AddFilmForm(request.POST)

        if film.is_valid():
            filled_form = film.save()
    return render(request, 'addFilm.html', context)


def home(request):
    return render(request, 'homepage.html',{})

def addDirector(request):
    context = {'form': AddDirectorForm}
    if request.method == 'POST':

        director = AddDirectorForm(request.POST)

        if director.is_valid():
            filled_form = director.save()
    return render(request, 'addDirector.html', context)



from re import A
from django.shortcuts import render
from .models import Director, Film
from films.forms import AddDirectorForm, AddFilmForm
from django.shortcuts import redirect

# Create your views here.

def addFilm(request):
    context = {'form': AddFilmForm}
    if request.method == 'POST':

        film = AddFilmForm(request.POST)

        if film.is_valid():
            filled_form = film.save()

    return render(request, 'addFilm.html', context)


def home(request):

    context = {'films':Film.objects.all()}

    return render(request, 'homepage.html',context)

def addDirector(request):
    context = {'form': AddDirectorForm}
    if request.method == 'POST':

        director = AddDirectorForm(request.POST)

        if director.is_valid():
            filled_form = director.save()
    return render(request, 'addDirector.html', context)

def update_film(request,id):
    film= Film.objects.all()
    form = AddFilmForm(instance = film)
    context = {'form':form}

    if request.method =='POST':
        filled_form = AddFilmForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect ('homepage')
        else:
            return redirect ('update_film',args=[id])
    return render (request, 'update_film.html',context)
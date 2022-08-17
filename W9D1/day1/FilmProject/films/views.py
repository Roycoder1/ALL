

from re import A
from django.shortcuts import render
from .models import Director, Film
from films.forms import AddDirectorForm, AddFilmForm
from django.shortcuts import redirect
from django.views import generic

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


class homepage(generic.ListView):
    template_name = 'homepage.html'
    context_object_name: "films"
    model = Film
    

def addDirector(request):
    context = {'form': AddDirectorForm}
    if request.method == 'POST':

        director = AddDirectorForm(request.POST)

        if director.is_valid():
            director.save()
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


def update_director(request,id):
    director= Director.objects.all()
    form = AddDirectorForm(instance = director)
    context = {'form':form}

    if request.method =='POST':
        filled_form = AddDirectorForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect ('homepage')
        else:
            return redirect ('update_director',args=[id])
    return render (request, 'update_director.html',context)

# class DirectorFilm(generic.ListView):
#     template_name = 'update_director.html'
#     context_object_name = "films"
#     model = Director

#     def get_context_data(self,id) :
#         context = si



    
        
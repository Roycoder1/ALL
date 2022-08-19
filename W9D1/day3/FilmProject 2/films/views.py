from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import FilmForm, DirectorForm
from .models import Director, Film
from datetime import date
from django.views import generic
from django.contrib import messages
from django import forms
from django.http import HttpResponseForbidden

# Create your views here.

context = {'films': Film.objects.all(), 'directors': Director.objects.all()}



class Homepage(generic.ListView):
    template_name = 'homepage.html'
    context_object_name = "films"
    form_class = FilmForm
    model = Film
    
    def get_form(self, form_class):
            form = super(Homepage, self).get_form(form_class)
            form.fields['release_date'].widget = forms.DateInput(attrs={'type':'date'})
            return form


@user_passes_test(lambda u: u.has_perm('films.can_add_film'))
def add_film(request):
    context.update({'form': FilmForm(initial={'release_date': date.today()})})

    if request.method == 'POST':
        form_filled = FilmForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('homepage')
        else:
            print(form_filled.errors)
    
    return render(request, 'add_film.html', context)


class AddFilm(generic.CreateView):
    model = Film
    fields = "__all__"
    template_name = "add_film.html"
    success_url = 'homepage'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('films.can_add_film'):
            messages.add_message(request, messages.ERROR, "User Doesnt have PERMISSIONS!")     
            return redirect('homepage')   
        return super().dispatch(request, *args, **kwargs)


@login_required(login_url='signin')
def add_director(request):
    context.update({'form': DirectorForm})

    if request.method == 'POST':
        form_filled = DirectorForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('homepage')
        else:
            print(form_filled.errors)
    
    return render(request, 'add_director.html', context)    


@login_required(login_url='signin')
def update_director(request, id):
    dir = Director.objects.get(id=id)
    form = DirectorForm(request.POST or None, instance=dir)
    context.update({'form': form})
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Director updated successfully")
        return redirect('homepage')

    return render(request, 'update_director.html', context)


@login_required(login_url='signin')
def update_film(request, id):
    film = Film.objects.get(id=id)
    form = FilmForm(request.POST or None, instance=film)
    context.update({'form': form})
    if form.is_valid():
        form.save()
        return redirect('homepage')
    return render(request, 'update_film.html', context)




def director_films(request, id):
    director = Director.objects.get(id=id)
    films = director.films.all()
    context.update({'director': director,'films': films})

    return render(request, 'director_films.html', context)


# class DirectorFilms(generic.ListView):

#     template_name = 'director_films.html'
#     context_object_name = "films"
#     model = Director

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        
#         context = sup













def dynamic_articles_view(request):
    dir = Director.objects.filter(first_name__icontains=request.GET.get('search')).first()
    return redirect('director_films', args=[dir.id])

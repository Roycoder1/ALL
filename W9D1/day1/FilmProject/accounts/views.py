from ast import Delete
from datetime import date
from multiprocessing import context
from django.shortcuts import render

from accounts.models import UserProfile


# Create your views here.
from xml.dom.expatbuilder import FilterVisibilityController
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import ProfileForm
from .models import UserProfile
from films.forms import AddFilmForm

# Create your views here.

def signup(request):
    context = {'form': UserCreationForm}
    if request.method == 'POST':
        print("POST")
        form_filled = UserCreationForm(request.POST)
        if form_filled.is_valid():
            
            form_filled.save()

            username = form_filled.cleaned_data.get('username')
            password = form_filled.cleaned_data.get('password1')
            # Authentiacate
            user = authenticate(username=username, password=password)
            
            #create profile here
            # UserProfile.objects.create(user_id = user.id)

            
            # user = form_filled.save()

            # regulars = Group.objects.get(name='Regulars')
            # regulars.user_set.add(user)

            login(request, user)
            return redirect('homepage')

        else:
            return render(request, 'signup.html', {'form': form_filled})

    return render(request, 'signup.html', context)

def signin(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authernticate
        user = authenticate(username = username, password = password)
        if user is not None:
            # login takes request and the user associated
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'signin.html', {'form': AuthenticationForm(request.POST)})
    
    else:
        return render(request, 'signin.html', {'form': AuthenticationForm})


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('signin')


def update_profile(request):
    profile = request.user.userprofile
    form = ProfileForm(request.POST or None , instance = profile)
    context={'form':form}
    if form.is_valid():
        form.save()
        return redirect('profile')
    
    return render(request , 'update_profile.html' , context)
    
    

def profile_user(request):
    user = UserProfile.objects.all()
    context = {'user': user}
    return render(request,"profile.html",context)

def profile(request):
    user = request.user
    profile = user.userprofile
    context = {'profile': profile}

    return render(request, 'profile.html', context)

(lambda u:u.has_perm('films.can_delete_film'))

def delete_film(request):
    context = {'form': AddFilmForm (initial={'released_date': date.today})}
    if request.method == 'POST':
        form_filled = AddFilmForm(request.POST)
        if form_filled.is_valid():
            form_filled.delete()
            return redirect ('homepage')
        else:
            print(form_filled.errors)

    return render(request,'delete_film.html',context)


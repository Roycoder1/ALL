from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import UserProfile


# Create your views here.
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

def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('signin')

def profile(request):

    user = request.user
    # profile = user.userprofile     
    context = {'profile': profile}

    return render(request, 'profile.html', context)




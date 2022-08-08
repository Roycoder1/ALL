from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile, Posts

def index(request):

    return HttpResponse("This is index here")

def profile(request):

    return HttpResponse("This is user profile here")


def posts(request, author_id: int) -> HttpResponse:
    user = UserProfile.objects.get(id = author_id) # -> UserProfile
    posts = user.posts.all() # -> QuerySet
    return render(request, 'posts.html', {'posts': posts})

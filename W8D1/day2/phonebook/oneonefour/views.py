from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# get person by name
def get_by_name(request, name: str) -> HttpResponse:
    person = Person.objects.get(name = name)
    return render(request, 'info.html', {'person': person})

# get person by number
def get_by_number(request, number: str) -> HttpResponse:
    person = Person.objects.get(phone_number = number)
    return render(request, 'info.html', {'person': person})

# get all persons
def get_all(request):
    persons = Person.objects.all()
    return render(request, 'all.html', {'persons': persons})
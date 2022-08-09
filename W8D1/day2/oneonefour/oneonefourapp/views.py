from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.
#get person by name
def get_by_name(request,name):
    person = Person.objects.get(name=name)
    return render (request, 'info.html',{'person':person})

def get_by_number(request,number):
    person = Person.objects.get(phone_number= person)
    return render (request, 'info.html',{'person' : person})

def get_all(request):
    persons = Person.objects.all()
    return render (request, 'all.html',{'persons':persons})
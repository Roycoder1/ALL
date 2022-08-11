from django.shortcuts import render
from .models import Family, Animal

# Create your views here.
def index(request):
    family_selected = Family.objects.get(id = id)
   
    return render(request,'index.html',family_selected)

def animal(request):
    animal_selected = Animal.objects.get(id=id)

    return render(request,'animal.html',animal_selected)

def animals (request):
    return render (request,'animals.html')
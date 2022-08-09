from django.shortcuts import render
from .models import Family, Animal

# Create your views here.
def index(request):
    id = Family.objects.get(id = id)
   
    return render(request,'index.html',{'id':id})

def animal(request):


    return render(request,'animal.html')

def animals (request):
    return render (request,'animals.html')
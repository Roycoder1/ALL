from django.shortcuts import render
from models import Family
from models import Animal

# Create your views here.
def index(request):
    x = Family.objects.get(id = id)
    print (x)
    if x == Animal.objects.get(id = id):
        {Animal.legs,Animal.weight,Animal.height,Animal.speed,Animal.family}
    return render(request,'index.html')

def animal(request):


    return render(request,'animal.html')

def animals (request):
    return render (request,'animals.html')
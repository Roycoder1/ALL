from unicodedata import name
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render # this line is added automatically
from .models import Daily
from .forms import dailyForm

def daily(request):
    daily = Daily()
    context = {
        'name' : daily.name,
        'adress' : daily.adress,
        'city' : daily.city,
        'country': daily.country
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = dailyForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            post_to_add = form.save(commit=False) 
            # will return an object that hasn’t yet been saved to the database
            for attr, value in post_to_add.__dict__.items():
                print(f'{attr} : {value}')

            return render(request, 'daily.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'daily.html', context)

    else:
        # GET, generate blank form
        context['form'] = dailyForm()
    return render(request, 'daily.html', context)
from distutils.command.upload import upload
from unicodedata import category, name
from django.shortcuts import render
from .models import Gif,Category

from .forms import CategoryForm, GifForm
# Create your views here.

def get_gif(request):
    allgifs = Gif.objects.all()
    
    return render(request, "gifs.html", {'allgifs': allgifs})




def index(request):
    context = {
        'page_title' : "Homepage\n",
        'user' : name ,
        'form' : GifForm ,
    }
    return render(request, 'homepage.html', context)

def create_category(request):
    if request.method == "POST":
        form_filled = CategoryForm(request.POST)
        form_filled.is_valid()
        if form_filled.is_valid():
            name = form_filled.cleaned_data ['name']
            
            Category.objects.create(name=name)

    # method : get

    context = {'form': CategoryForm}
    return render (request, 'create_category.html',context)

def create_gif(request):
    if request.method == 'POST':
       form_field = GifForm(request.POST)
       if form_field.is_valid():
        title = form_field.cleaned_data['title']
        url = form_field.cleaned_data['url']
        uploader = form_field.cleaned_data['uploader_name']

        categories = form_field.cleaned_data ['categories']

        new_gif = Gif(title = title , url =url , uploader_name = uploader)
        new_gif.save()
        for cat in categories:
            new_gif.categories.add(cat)
        new_gif.save()


    context = {'form' :GifForm}
    return render(request,'create_gif.html',context)

def category_view(request,id):
    category = Category.objects.get(id=id)
    gifs = category.gifs.all()

    context = {"category":category , 'gifs': gifs}

    return render(request, "category.html",context)


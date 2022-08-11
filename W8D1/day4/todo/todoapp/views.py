from multiprocessing import context
from unicodedata import category
from django.shortcuts import render

from todoapp.models import Category, Todo
from .forms import CategoryForm, Todoform

# Create your views here.
def todo(request):
     if request.method == "POST":
        form_filled = Todoform(request.POST)
        form_filled.is_valid()
        if form_filled.is_valid():
            title = form_filled.cleaned_data ['title']
            details = form_filled.cleaned_data ['details']
            has_been_done = form_filled.cleaned_data ['has_been_done']
            date_creation = form_filled.cleaned_data ['date_creation']
            date_completion = form_filled.cleaned_data ['date_completion']
            deadline_date = form_filled.cleaned_data ['deadline_date']
            Todoform.objects.create(title=title,details=details,has_been_done=has_been_done,date_creation=date_creation,date_completion=date_completion,deadline_date=deadline_date)

    # method : get

     context = {'form': Todoform}
     return render(request, 'todo.html',context)

def display_todos(request):
    categories = Category.objects.all()
    image= categories.clean_data['image']
    list = Todo.objects.all()
    context= {'categories':categories,'list':list}
    return render(request,'all.html',context)

def create_todo(request):
    context= {'form': Todoform}

    if request.method =='POST':
        form_filled = Todoform(request.POST)
        if form_filled.is_valid():
            title = form_filled.cleaned_data['title']
            details = form_filled.cleaned_data ['details']
            deadline_date = form_filled.cleaned_data['deadline_date']
            category = form_filled.cleaned_data['category']

            Todo.objects.create(title = title,details=details,deadline_date=deadline_date,category=category)

    return render (request,'add_todo.html',context)

def create_category(request):
    context = {'form':CategoryForm}
    if request.method =='POST':
        form_filled =CategoryForm(request.POST)
        if form_filled.is_valid():
            name = form_filled.cleaned_data['name']
            image = form_filled.cleaned_data['image']

        Category.objects.create(name=name,image=image)
        return render(request,'add_category.html',context)



def home(request):
    categories = Category.objects.all()
    context = {'categories':categories}

    return render(request,'home.html',context)

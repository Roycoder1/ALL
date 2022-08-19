
from django.shortcuts import render,redirect

from .forms import VacanciesForm,MoreInfo
from .models import Visitor
# Create your views here.
def display_info(request):
    display = Visitor.objects.all()
    context = {'info': display}
    return render(request, 'homepage.html', context)

def vacancies(request):
    context = {'form': VacanciesForm}
    if request.method == 'POST':

        date = VacanciesForm(request.POST)

        if date.is_valid():
            date.save()
            return redirect("homepage")
    return render(request, 'availability.html', context)

def more_info(request):
    context = {'form':MoreInfo}
    if request.method =='POST':
        info = MoreInfo(request.POST)

        if info.is_valid():
            info.save()
            return redirect("homepage")
    return render(request,'info.html',context)
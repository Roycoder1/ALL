from django.shortcuts import render

from real_estate_app.forms import RegistrationForm, homeForm,InquiryForm


# Create your views here.
def home(request):
    context = {'form': homeForm}
    if request.method == 'POST':
        print("POST")
        form_filled = homeForm(request.POST)
        if form_filled.is_valid():
            
            form_filled.save()

            

    return render(request, 'home.html', context)

def listing(request):
    context = {'form': InquiryForm}
    if request.method == 'POST':
        
        form_filled = InquiryForm(request.POST)
        if form_filled.is_valid():
            
            form_filled.save()

    return render (request,'listing.html',context)

def listing2(request):
    context = {'form': InquiryForm}
    if request.method == 'POST':
        
        form_filled = InquiryForm(request.POST)
        if form_filled.is_valid():
            
            form_filled.save()

    return render (request,'home2_list.html',context)

def listing3(request):
    context = {'form': InquiryForm}
    if request.method == 'POST':
        
        form_filled = InquiryForm(request.POST)
        if form_filled.is_valid():
            
            form_filled.save()

    return render (request,'home3_list.html',context)

def listing4(request):
    context = {'form': InquiryForm}
    if request.method == 'POST':
        
        form_filled = InquiryForm(request.POST)
        if form_filled.is_valid():
            
            form_filled.save()

    return render (request,'home4_list.html',context)

   

def listing5(request):
    context = {'form': InquiryForm}
    if request.method == 'POST':
        
        form_filled = InquiryForm(request.POST)
        if form_filled.is_valid():
            
            form_filled.save()

    return render (request,'home5_list.html',context)



def listing6(request):
    context = {'form': InquiryForm}
    if request.method == 'POST':
        
        form_filled = InquiryForm(request.POST)
        if form_filled.is_valid():
            
            form_filled.save()

    return render (request,'home6_list.html',context)

   


def about(request):
    return render(request,'about.html')

def search(request):
    return render(request,'search.html')


def register(request):
    context = {'form':RegistrationForm}
    if request.method == 'POST':
        
        form_filled = RegistrationForm(request.POST)
        if form_filled.is_valid():
            print('valid')
            form_filled.save()
        else:
            print(form_filled.errors)
    return render(request, 'register.html', context)

def dashboard(request):
    user = request.user
    # profile = user.userprofile     
    context = {'user': user}

    return render(request,'dashboard.html',context)

def listings(request):
    return render(request, 'listings.html')

def list_details(request,id):
    listed_house=home
from ast import Raise
from ssl import VERIFY_CRL_CHECK_LEAF

from django.shortcuts import render
from faker import Faker
from .forms import addVehicle, formAdd

from bike_app.models import Category, Customer, Rental, Vehicle
# Create your views here.

def Fake(request):

    fake= Faker()
    # fake.name()
    for i in range(100):
        customer = Customer(first_name = fake.first_name(), last_name = fake.last_name(), email = fake.email(), phone_number = fake.phone_number(), adress = fake.address(), city = fake.city(), country = fake.country())
        customer.save()
    return render(request, 'index.html')

def show_details(request):
    # order it by rental_date
    rental = Rental.objects.all().order_by('rental_date')
    context = {"rental":rental}
    return render(request,'rental.html',context)

def rental_details(request):
    #get rental,vehicle,customer
    rental = Rental.objects.all()
    vehicle = Vehicle.objects.all()
    customer= Customer.objects.all()
    context = {"rental": rental, "vehicle":vehicle,"customer": customer}

    return render(request, "details.html",context)


def rental_add(request):

    context = {'form':formAdd}

    if request.method == 'POST':
        form_filled = formAdd(request.POST)
        
        if form_filled.is_valid():
            customer_id = form_filled.cleaned_data['customer_id']
            vehicle_id = form_filled.cleaned_data['vehicle_id']
           
            Rental.objects.create(customer_id=customer_id,vehicle_id=vehicle_id)
            print("Vehicle already in sale")
        else:
            print('They should be an error mate!')

    return render(request, 'add.html', context)

def customers (request,id):
    customer = Rental.objects.get(id= formAdd.customer_id)
    customer.save()

    context = {'customer': customer}

    return render(request,'customer.html',context)

def customer_order(request):

    customer= Customer.objects.all().order_by('first_name')
    context = {"customer":customer}
    return render(request,'order.html',context)

def vehicle(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles':vehicles}
    return render(request,'vehicle.html',context)

def vehicle_id(request,id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    context = {"vehicle":vehicle}
    return render (request,"vehicle_id.html",context)

def vehicle_add(request):

    context = {'form': addVehicle}

    if request.method == 'POST':
        form_filled = addVehicle(request.POST)
        if form_filled.is_valid():
            vehicle_name = form_filled.cleaned_data['vehicle_name']
            cost = form_filled.cleaned_data['cost']
            Category.objects.create(vehicle_name=vehicle_name, cost=cost)

    return render(request, 'add_vehicle.html', context)

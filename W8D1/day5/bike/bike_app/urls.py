
from django.contrib import admin
from django.urls import path


from bike_app.views import Fake, customer_order, customers, rental_add, rental_details, show_details, vehicle, vehicle_add, vehicle_id

urlpatterns = [
    path("",Fake, name = 'Fake' ),
    path('rental',show_details, name= 'show_rental_details'),
    path('details', rental_details, name='details'),
    path('add',rental_add, name = 'add'),
    path('customer', customers,name = 'customer'),
    path('order', customer_order, name = 'order'),
    path('vehicle', vehicle , name='vehicle' ),
    path('vehicle_id',vehicle_id,name = 'vehicle_id'),
    path('add_vehicle',vehicle_add,name = 'add_vehicle')

]
from django.contrib import admin

from bike_app.models import Category, Customer, Rental, Rental_Rate, Vehicle, Vehicle_size, Vehicle_type

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Vehicle_type)
admin.site.register(Vehicle_size)
admin.site.register(Vehicle)
admin.site.register(Rental)
admin.site.register(Rental_Rate)
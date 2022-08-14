
from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

class Vehicle_type(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name


class Vehicle_size(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name



class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_type,on_delete=models.CASCADE, related_name='vehicle')
    date_created = models.DateTimeField()
    real_cost = models.IntegerField()
    size = models.ForeignKey(Vehicle_size, on_delete=models.CASCADE, related_name='size')
    def __str__(self) -> str:
        return f'{self.vehicle_type}  {self.size}'

    def get_absolute_url(self):
        return reverse('vehicleNew', args=[self.id])



class Rental(models.Model):
    rental_date= models.DateTimeField()
    return_date = models.DateTimeField()
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')
    vehicle= models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle')
    def __str__(self) -> str:
        return f'{self.rental_date}  {self.return_date}'


class Rental_Rate(models.Model):
    daily_rate = models.IntegerField()
    vehicle_type= models.ForeignKey(Vehicle_type, on_delete=models.CASCADE,related_name='type')
    vehicle_size = models.ForeignKey(Vehicle_size, on_delete=models.CASCADE,related_name='vsize')
    
class Category(models.Model):

    vehicle_name = models.CharField(max_length=50, unique=True)
    cost = models.IntegerField()

    def __str__(self) -> str:
        return self.vehicle_name
    
    def get_absolute_url(self):
        return reverse('category', args = [self.id])
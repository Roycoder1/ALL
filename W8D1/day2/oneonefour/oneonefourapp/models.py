import email
from pyexpat import model
from django.db import models

# Create your models here.
class Person (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    adress = models.CharField(max_length = 100)
    def __str__(self) -> str:
        return self.name+ ' '+self.phone_number
from email.message import Message

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class home(models.Model):
    Keyword = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Bedrooms = models.IntegerField()
    max_Price = models.IntegerField()

class Inquiry(models.Model):
    property = models.CharField(max_length=160)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Message = models.TextField()



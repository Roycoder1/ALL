from tkinter import CASCADE
from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=50)
    

class Animal(models.Model):
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    family = models.ForeignKey(Family , on_delete=models.CASCADE)


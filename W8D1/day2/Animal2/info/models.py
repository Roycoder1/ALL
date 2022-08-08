from django.db import models

# Create your models here.
class Animal(models.Model):
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    family = models.CharField(max_length=40)
    

class Family(models.Model):
    name = models.CharField(max_length=50)
from pyexpat import model
from django.db import models

# Create your models here.

class Daily(models.Model):
    name = models.CharField(max_length=60)
    adress = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
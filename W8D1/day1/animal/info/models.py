from django.db import models

# Create your models here.
class UserProfile(models.Model):

    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    adress = models.CharField(max_length=100, null = True)

    def __str__(self):
        return self.first_name

    
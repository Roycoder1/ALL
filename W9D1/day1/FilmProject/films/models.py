from tkinter import CASCADE, Widget
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self) -> str:
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self) -> str:
        return self.name


class Director(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def save(self,*args,**kwargs):
        same_dir = Director.objects.get(first_name = self.first_name,last_name = self.last_name)
        if same_dir :
            raise ValidationError("Can't add duplicate")
        else:
            self.super(Director,self).save(*args,**kwargs)

class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    created_in_country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    available_in_countries = models.ManyToManyField(Country, related_name="available")
    categories = models.ManyToManyField(Category, related_name="category")
    director= models.ManyToManyField(Director, related_name="director")

    def __str__(self) -> str:
        out = f'''
        {self.title}
        {self.release_date}
        '''
        for category in self.categories.all():
            out+=f'\n{str(category)}'
        out += "\n Director"
        for dir in self.director.all():
            out+=f'\n{str(dir)}'
        
        out+= f"\n Released: {self.release_date}"
        return out

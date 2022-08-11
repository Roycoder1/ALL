from audioop import reverse
from unicodedata import category
from unittest.mock import DEFAULT
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()

    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse ('category', args =[self.id])

class Todo (models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    has_been_done= models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(null=True)
    deadline_date = models.DateTimeField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title




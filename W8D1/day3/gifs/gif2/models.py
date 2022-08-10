from audioop import reverse
from django.db import models

# Create your models here.
class Gif (models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    uploader_name = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse('show_gif',args = [self.id])
        
  

class Category (models.Model):
    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField(Gif)
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse('show_gif',args = [self.id])
    
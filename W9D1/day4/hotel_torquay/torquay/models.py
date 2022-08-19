from django.db import models
# from django.contrib.gis.db.models import PointField





# Create your models here.

class Visitor(models.Model):
    # location = PointField(geography=True, spatial_index=True)
    images = models.URLField()
    description = models.TextField()
    area = models.TextField()
   
class Vacancies(models.Model):
    date1 = models.DateField()
    date2 = models.DateField()

class moreInfo(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=50)
    demand_subject = models.CharField(max_length=80)
    details = models.TextField(max_length=600)


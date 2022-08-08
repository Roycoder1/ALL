
from django.contrib import admin
from .models import Animal
from .models import Family #import the Person model


# Register your models here.
admin.site.register(Animal)
admin.site.register(Family)
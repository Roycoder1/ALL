from dataclasses import fields
from tkinter import Widget
from .models import Daily
from django import forms

class dailyForm(forms.ModelForm):
    class Meta:
      model = Daily
      fields = '__all__'
      widgets={
        'name': forms.Textarea(attrs={'class': 'name'}),
        'adress': forms.Textarea(attrs={'class': 'textarea'}),
        'city': forms.Select(attrs={'class': 'city'}),
        'country':forms.Select(attrs={'class': 'country'})
      }



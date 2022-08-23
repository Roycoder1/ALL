
from django import forms
from .models import home,Inquiry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class homeForm(forms.ModelForm):
    class Meta:
        model = home
        fields ='__all__'

class RegistrationForm(UserCreationForm):

    
    class Meta:
        model = User
        fields = ['first_name', 'last_name',"username", "email", "password1", "password2"]

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields='__all__'
    widgets={
         'Name': forms.Textarea(attrs={'class' : 'name' , 'rows':1})
    }
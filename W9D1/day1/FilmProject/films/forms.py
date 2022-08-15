
from .models import Director, Film
from datetime import date
from django import forms

class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title','release_date']
        widgets = {

            'release_date': forms.DateInput(attrs={'type' : 'date'})
        }


class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
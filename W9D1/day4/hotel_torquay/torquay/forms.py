
from django import forms
from .models import Vacancies,moreInfo

class VacanciesForm(forms.ModelForm):
   class Meta:
    model = Vacancies
    fields = '__all__'
    widgets={
       "date1": forms.DateInput(attrs={'type' : 'date'}),
       "date2": forms.DateInput(attrs={'type' : 'date'}),

    }
class MoreInfo(forms.ModelForm):
    class Meta:
        model = moreInfo
        fields = '__all__'
        widgets = {
            'first_name': forms.Textarea(attrs={'class' : 'fn'}),
            'last_name': forms.Textarea(attrs={'class' : 'ln'}),
            'city': forms.Textarea(attrs={'class' : 'city'}),
            'demand_subject': forms.Textarea(attrs={'class' : 'demand'}),
            'details': forms.Textarea(attrs={'class' : 'details'}),
            'email': forms.EmailInput(attrs={'class' : 'mail'}),
            'phone_number': forms.NumberInput(attrs={'class' : 'phone'})
        }
from distutils.command.upload import upload
from django import forms
from gif2.models import Category

class GifForm(forms.Form):
    name = forms.CharField()
    adress = forms.Textarea()
    age = forms.DateField(required=False)
    email = forms.EmailField()
    uploader_name = forms.CharField()
    title = forms.CharField()
    url = forms.URLField()
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

class CategoryForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=50)

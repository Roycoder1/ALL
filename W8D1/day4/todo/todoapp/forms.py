from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField()
    image = forms.URLField()


class Todoform(forms.Form):
    title = forms.CharField()
    details = forms.CharField()
    has_been_done= forms.CharField()
    date_creation = forms.DateTimeField(widget = forms.SelectDateWidget)
    date_completion = forms.DateTimeField(widget = forms.SelectDateWidget)
    deadline_date = forms.DateTimeField(widget = forms.SelectDateWidget)
    # category = forms.ModelChoiceField


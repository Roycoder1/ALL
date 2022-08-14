from django import forms

class formAdd(forms.Form):
    customer_id = forms.IntegerField()
    vehicle_id = forms.IntegerField()
    
class addVehicle(forms.Form):
    vehicle_name = forms.CharField()
    cost = forms.IntegerField()


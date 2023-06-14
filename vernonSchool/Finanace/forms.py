from django import forms 
class FeePayForm(forms.Form):
    name = forms.CharField() 
    Class = forms.IntegerField() 
    amount = forms.IntegerField()

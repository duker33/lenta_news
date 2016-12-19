from django import forms
from django.forms import DateInput


class OrderNewsForm(forms.Form):
    email = forms.EmailField()
    date_from = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

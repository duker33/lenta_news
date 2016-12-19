from django import forms
from django.forms import DateInput


class OrderNewsForm(forms.Form):
    email = forms.EmailField()
    date_from = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'placeholder': '2016-12-14'}))
    date_to = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'placeholder': '2016-12-19'}))

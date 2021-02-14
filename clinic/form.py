from django import forms
from django.forms.widgets import CheckboxInput

class name(forms.Form):
    numberLotto = forms.IntegerField(label='bet')
    top = forms.BooleanField(required=False)
    down = forms.BooleanField(required=False)
    price = forms.IntegerField(label='price')
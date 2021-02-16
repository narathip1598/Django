from django import forms
from django.forms.widgets import CheckboxInput, HiddenInput

class name(forms.Form):
    numberLotto = forms.IntegerField(label='bet')
    top = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    down = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    price = forms.IntegerField(label='price')
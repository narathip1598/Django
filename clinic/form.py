from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxInput, HiddenInput
from django.conf import settings
from django.db import models
from django.utils import timezone

class name(forms.Form):
    numberLotto = forms.IntegerField(label='bet')
    top = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    down = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    price = forms.IntegerField(label='price')

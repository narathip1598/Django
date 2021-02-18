from django import forms
from django.db import models

class formAdd(forms.Form):
    firstName = forms.CharField(max_length=50)
    lastName = forms.CharField(max_length=50)

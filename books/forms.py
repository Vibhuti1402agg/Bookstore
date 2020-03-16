from django import forms
from .models import info
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class registrationform(forms.Form):
    username=forms.CharField(max_length=20)
    email=forms.EmailField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput)

class addbook(forms.ModelForm):
    class Meta:
        model = info
        fields=('name','price','stock','image')

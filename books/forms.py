from django import forms
from .models import info
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,get_user_model

User=get_user_model()

class registrationform(forms.ModelForm):
    email=forms.EmailField(label='Email Address')
    password=forms.CharField(widget=forms.PasswordInput,label='Enter Password')
    password2=forms.CharField(widget=forms.PasswordInput,label='Confirm Password')

    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password',
            'password2',
        ]

    def clean(self,*args,**kwargs):
        email= self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords dont match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email already in use")
        return super(registrationform,self).clean(*args,**kwargs)

class loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise ValidationError('Username or Password Incorrect')
            if not user.check_password(password):
                raise ValidationError('Wrong Password')

        return super(loginform,self).clean(*args,**kwargs)


class addbook(forms.ModelForm):
    class Meta:
        model = info
        fields=('name','price','stock','image')




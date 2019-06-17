from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Post


class Login(forms.Form):
    Username=forms.CharField(max_length=20)
    Password=forms.CharField(widget=forms.PasswordInput,max_length=20)

    def clean(self):
        u=self.cleaned_data.get('Username')
        p=self.cleaned_data.get('Password')
        val=authenticate(username=u,password=p)
        if val is None:
            raise forms.ValidationError("Invalid Credentials")

class Register(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=20)
    Retype_password=forms.CharField(widget=forms.PasswordInput,max_length=20)
    email=forms.CharField(widget=forms.EmailInput)

    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

    def clean(self):
        x=super(Register,self).clean()
        p=x.get('password')
        p1=x.get('Retype_password')
        if p!=p1:
            self.add_error('Retype_password','Both Passwords dont Match')
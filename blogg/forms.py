from django import forms
from django.contrib.auth.models import User
from .models import Post

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name','last_name','username','password']

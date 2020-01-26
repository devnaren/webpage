from django import forms
from .models import UserModel
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','email','password']

class UserProfile(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['protfolios_site','profile_picture']

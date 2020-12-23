'''In this we need to compulsorily import Models from the models.py '''
from django import forms
from django.forms import ModelForm
from .models import Customer
from django.contrib.auth.models import User


class CustomerGetStartedForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # confirmPassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Customer
        fields = ('username','first_name','last_name','email','phone','password')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')

class CustomerEditForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('profile_image','phone','password')



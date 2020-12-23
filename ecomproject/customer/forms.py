'''In this we need to compulsorily import Models from the models.py '''
from django import forms
from django.forms import ModelForm
from .models import Customer
from django.contrib.auth.models import User

import django.utils.timezone as timezone
current_year = timezone.now().year

YEARS = [yy for yy in range(1940,current_year)] 

class CustomerGetStartedForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    dob = forms.DateField(label='Date Of Birth',initial="1990-01-01", widget=forms.SelectDateWidget(years=YEARS))
   
    class Meta:
        model = Customer
        fields = ('username','first_name','last_name','email','phone','dob','password')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')

class CustomerEditForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('profile_image','phone','password','dob')



'''In this we need to compulsorily import Models from the models.py '''
from django import forms
from django.forms import ModelForm
from .models import Customer


class CustomerGetStartedForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # confirmPassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Customer
        fields = '__all__'
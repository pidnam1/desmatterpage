from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User



class CompanySignUpForm(UserCreationForm):
    business_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    bio = forms.CharField(max_length=2000, required=False, help_text='Description of company')
    location = forms.CharField(max_length=100, required=False, help_text='State in which business operates')


    class Meta:
        model = User
        fields = ('username', 'business_name', 'email','bio', 'location',  'password1', 'password2')

class ManufacturerSignUpForm(UserCreationForm):
    business_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    bio = forms.CharField(max_length=2000, required=False, help_text='Description of company')
    location = forms.CharField(max_length=100, required=False, help_text='State in which business operates')
    size = forms.CharField(max_length=50, required= False, help_text='Size of the manufacturer')


    class Meta:
        model = User
        fields = ('username', 'business_name', 'email','bio', 'location', 'size', 'password1', 'password2')



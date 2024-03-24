from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from .models import ShipRecords

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# Create a User
class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']


# Create a Login 
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# model for crate records
class AddEntryForm(forms.ModelForm):

    class Meta:

        model =  ShipRecords
        fields = ['ShipName', 'ShipCurrentCaptain', 'ShipEmail', 'ShipMobile', 'ShipOriginCountry',
                'ShipOriginPort', 'ShipSize', 'ShipTotalIncident', 'ShipLastServiceDate', 'ShipCarbonEmission']
        

# model for update records
class UpdateEntryForm(forms.ModelForm):

    class Meta:

        model =  ShipRecords
        fields = ['ShipName', 'ShipCurrentCaptain', 'ShipEmail', 'ShipMobile', 'ShipOriginCountry',
                'ShipOriginPort', 'ShipSize', 'ShipTotalIncident', 'ShipLastServiceDate', 'ShipCarbonEmission']
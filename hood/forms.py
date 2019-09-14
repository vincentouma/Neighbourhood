from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['prof_user','profile_Id']



class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name','loc','occupants']

class BusinessForm(forms.ModelForm):
    class Meta:
        model  = Business
        fields = ['name','hood','email']        
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Kit, Strategy, CustomUser

class KitForm(ModelForm):
    class Meta: 
        model = Kit
        fields = ['date', 'strategy']

class StrategyForm(ModelForm):
    class Meta:
        model = Strategy
        fields = '__all__'

class UserForm(UserCreationForm):
    country = forms.CharField(label = "Country")

    class Meta:
        model = CustomUser
        fields = ['username', 'state']
from django.contrib.auth.models import User
from .models import Capacities

from django import forms


class CapacityForm(forms.ModelForm):
    capacity_value = forms.IntegerField(label='Pojemnosc w cm3')
    capacity_short = forms.DecimalField(label='Skrocona wartosc')

    class Meta:
        model: Capacities
        fields = ('capacity_value', 'capacity_short')



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

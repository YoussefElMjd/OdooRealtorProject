from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Client

class ClientForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name', 'last_name')

class ClientChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email','first_name', 'last_name')
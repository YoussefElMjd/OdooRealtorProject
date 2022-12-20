from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import OdooUser

class OdooUserForm(forms.Form):
    email = forms.CharField(label="Email", max_length=255)
    password = forms.CharField(label="Password", max_length=255, widget = forms.PasswordInput())
    class Meta:
        model = OdooUser
        fields = ('email', 'password')

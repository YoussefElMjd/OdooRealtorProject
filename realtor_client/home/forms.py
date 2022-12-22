from django import forms
from .models import OdooUser

class OdooUserForm(forms.Form):
    url = forms.CharField(label="URL", max_length=255)
    db = forms.CharField(label="db", max_length=255)
    email = forms.CharField(label="Email", max_length=255)
    password = forms.CharField(label="Password", max_length=255, widget = forms.PasswordInput())
    class Meta:
        model = OdooUser
        fields = ('url', 'db','email', 'password')

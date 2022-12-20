from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Client

from .forms import ClientForm, ClientChangeForm


class ClientAdmin(UserAdmin):
    add_form = ClientForm
    form = ClientChangeForm
    model = get_user_model()
    list_display = ('first_name', 'last_name', 'email', 'password')

admin.site.register(Client, ClientAdmin)

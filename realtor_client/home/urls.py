from django.urls import path

from .views import HomeView, LoginView
from . import models

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', LoginView.as_view(), name="login"),
]
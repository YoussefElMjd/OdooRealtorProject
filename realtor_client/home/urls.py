from django.urls import path

from .views import HomeView, LoginView
from . import models

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', models.create, name='create'),
    path('login', LoginView.as_view(), name="login"),
    path('loginAuth', models.authenticate, name="loginAuth"),
    path('test', models.set_offer, name="test"),

]
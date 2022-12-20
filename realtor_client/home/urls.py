from django.urls import path

from .views import HomeView
from . import views

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', views.create, name='create'),
]
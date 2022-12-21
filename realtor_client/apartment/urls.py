from django.urls import path
from . import models

app_name = 'apartment'

urlpatterns = [
    path('', models.authenticate, name="apartment"),
    path('offer', models.set_offer, name="offer"),
]
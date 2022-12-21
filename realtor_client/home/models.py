from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import xmlrpc.client
from django.shortcuts import render

class OdooUser(models.Model):  
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)



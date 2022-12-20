from django.shortcuts import render
from django.views.generic import TemplateView
from .models import OdooUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .forms import OdooUserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth import authenticate

class HomeView(TemplateView):
    template_name = "home/index.html"
    model = OdooUser
    context_object_name = 'odooUsers'
    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        context['form'] = OdooUserForm
        return context

class LoginView(TemplateView):
    template_name = "home/login.html"
    model = OdooUser
    context_object_name = 'odooUsers'
    def get_context_data(self, **kwargs):
        context = super(LoginView,self).get_context_data(**kwargs)
        context['form'] = OdooUserForm
        return context

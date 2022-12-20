from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Client
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .forms import ClientForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home/index.html"
    model = Client
    context_object_name = 'clients'
    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        context['form'] = ClientForm
        return context

def create(request):
    form = ClientForm(request.POST)
    Client.objects.create(
        username=request.POST['username'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=['password1'],
        )
    return HttpResponseRedirect("/")
from django.views.generic import TemplateView
from .models import OdooUser
from .forms import OdooUserForm
from django.views.generic import TemplateView

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

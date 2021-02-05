from django.shortcuts import render
from django.views import generic

# Importo mixines para importar el logeo de django
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here. LoginRequiredMixin => es para importar el comportamiento de login
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name='bases/home.html'
    login_url='bases:login'
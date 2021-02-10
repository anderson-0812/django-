from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy ## redireccionar a otro sitio
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Cliente
from .forms import ClienteForm
from bases.views import SinPrivilegios

class ClienteView(LoginRequiredMixin,generic.ListView):
    model = Cliente
    template_name = "cliente/cliente_list.html"
    context_object_name = "obj"
    login_url="bases:login"
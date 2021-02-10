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

class ClienteNew(LoginRequiredMixin,generic.CreateView):
    model=Cliente
    template_name="cliente/cliente_form.html"
    context_object_name = "obj"
    form_class=ClienteForm
    success_url=reverse_lazy("cliente:cliente_list") ##se deeb importa reverse_lazy
    login_url="bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ClienteEdit(LoginRequiredMixin,generic.UpdateView):
    model=Cliente
    template_name="cliente/cliente_form.html"
    context_object_name = "obj"
    form_class=ClienteForm
    success_url=reverse_lazy("cliente:cliente_list")
    login_url="bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ClienteDel(LoginRequiredMixin, generic.DeleteView):
    model=Cliente
    template_name='cliente/cliente_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("cliente:cliente_list")
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria, SubCategoria
from .forms import CategoriaForm, SubCategoriaForm

from bases.views import SinPrivilegios
from django.contrib.messages.views import SuccessMessageMixin



class CategoriaView(LoginRequiredMixin,generic.ListView):
    model = Categoria
    template_name = "inventario/categoria_list.html"
    context_object_name = "obj"
    login_url="bases:login"

class CategoriaNew(LoginRequiredMixin,generic.CreateView):
    model=Categoria
    template_name="inventario/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inventario:categoria_list") ##se deeb importa reverse_lazy
    login_url="bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin,generic.UpdateView):
    model=Categoria
    template_name="inventario/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inventario:categoria_list")
    login_url="bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model=Categoria
    template_name='inventario/categoria_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inventario:categoria_list")


class SubCategoriaView(SinPrivilegios, \
    generic.ListView):
    permission_required = "inventario.view_subcategoria"
    model = SubCategoria
    template_name = "inventario/subcategoria_list.html"
    context_object_name = "obj"


class SubCategoriaNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView):
    model=SubCategoria
    template_name="inventario/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inventario:subcategoria_list")
    success_message="Sub Categoría Creada Satisfactoriamente"
    permission_required="inventario.add_subcategoria"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView):
    model=SubCategoria
    template_name="inventario/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inventario:subcategoria_list")
    success_message="Sub Categoría Actualizada Satisfactoriamente"
    permission_required="inventario.change_subcatetoria"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(SuccessMessageMixin,SinPrivilegios, generic.DeleteView):
    model=SubCategoria
    template_name='inventario/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inventario:subcategoria_list")
    success_message="Sub Categoría Eliminada"
    permission_required="inventario.delete_subcategoria"
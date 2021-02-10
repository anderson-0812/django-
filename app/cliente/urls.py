from django.urls import path

from .views import ClienteView, ClienteNew, ClienteEdit

urlpatterns = [
    path('cliente/',ClienteView.as_view(), name='cliente_list'),   
    path('cliente/new',ClienteNew.as_view(), name='cliente_new'),
    path('cliente/edit/<int:pk>',ClienteEdit.as_view(), name='cliente_edit'),
    # path('cliente/del/<int:pk>',ClienteDel.as_view(), name='cliente_del'),


]
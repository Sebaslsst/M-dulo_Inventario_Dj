from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Insumo, Pedido, Proveedor


# Vista para listar Insumos
class InsumoListView(ListView):
    model = Insumo
    template_name = 'insumo_list.html'
    context_object_name = 'insumos'


# Vista para ver el detalle de un Insumo
class InsumoDetailView(DetailView):
    model = Insumo
    template_name = 'insumo_detail.html'
    context_object_name = 'insumo'


# Vista para crear un nuevo Insumo
class InsumoCreateView(CreateView):
    model = Insumo
    template_name = 'insumo_form.html'
    fields = ['identificador', 'nombre', 'cantidadDisponible', 'unidadMedida', 'nivelReorden', 'fechaVencimiento',
              'precioUnitario', 'ubicacion']
    success_url = reverse_lazy('insumo_list')


# Vista para actualizar un Insumo existente
class InsumoUpdateView(UpdateView):
    model = Insumo
    template_name = 'insumo_form.html'
    fields = ['identificador', 'nombre', 'cantidadDisponible', 'unidadMedida', 'nivelReorden', 'fechaVencimiento',
              'precioUnitario', 'ubicacion']
    success_url = reverse_lazy('insumo_list')


# Vista para eliminar un Insumo
class InsumoDeleteView(DeleteView):
    model = Insumo
    template_name = 'insumo_confirm_delete.html'
    success_url = reverse_lazy('insumo_list')


# Vista para listar Pedidos
class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedido_list.html'
    context_object_name = 'pedidos'


# Vista para listar Proveedores
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedor_list.html'
    context_object_name = 'proveedores'

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Insumo, Proveedor, Pedido


# --- Vistas para el modelo Insumo ---
class InsumoListView(ListView):
    model = Insumo
    template_name = 'insumo_list.html'  # La plantilla que se utilizará
    context_object_name = 'insumos'  # Nombre del contexto para acceder en la plantilla


class InsumoDetailView(DetailView):
    model = Insumo
    template_name = 'insumo_detail.html'
    context_object_name = 'insumo'


class InsumoCreateView(CreateView):
    model = Insumo
    template_name = 'insumo_form.html'
    fields = ['identificador', 'nombre', 'cantidadDisponible', 'unidadMedida',
              'nivelReorden', 'fechaVencimiento', 'precioUnitario', 'ubicacion']
    success_url = reverse_lazy('insumo_list')  # Redirigir a la lista de insumos después de crear


class InsumoUpdateView(UpdateView):
    model = Insumo
    template_name = 'insumo_form.html'
    fields = ['identificador', 'nombre', 'cantidadDisponible', 'unidadMedida',
              'nivelReorden', 'fechaVencimiento', 'precioUnitario', 'ubicacion']
    success_url = reverse_lazy('insumo_list')


class InsumoDeleteView(DeleteView):
    model = Insumo
    template_name = 'insumo_confirm_delete.html'
    success_url = reverse_lazy('insumo_list')


# --- Vistas para el modelo Proveedor ---
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedor_list.html'
    context_object_name = 'proveedores'


class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'proveedor_detail.html'
    context_object_name = 'proveedor'


class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = 'proveedor_form.html'
    fields = ['nombre', 'email', 'direccion', 'contacto']
    success_url = reverse_lazy('proveedor_list')


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = 'proveedor_form.html'
    fields = ['nombre', 'email', 'direccion', 'contacto']
    success_url = reverse_lazy('proveedor_list')


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')


# --- Vistas para el modelo Pedido ---
class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedido_list.html'
    context_object_name = 'pedidos'


class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detail.html'
    context_object_name = 'pedido'


class PedidoCreateView(CreateView):
    model = Pedido
    template_name = 'pedido_form.html'
    fields = ['cliente', 'fecha', 'estado']
    success_url = reverse_lazy('pedido_list')


class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = 'pedido_form.html'
    fields = ['cliente', 'fecha', 'estado']
    success_url = reverse_lazy('pedido_list')


class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'pedido_confirm_delete.html'
    success_url = reverse_lazy('pedido_list')

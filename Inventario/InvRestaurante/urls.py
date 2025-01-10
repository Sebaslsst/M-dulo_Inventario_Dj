from django.urls import path
from .views import (
    InsumoListView, InsumoDetailView, InsumoCreateView, InsumoUpdateView, InsumoDeleteView,
    ProveedorListView, ProveedorDetailView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView,
    PedidoListView, PedidoDetailView, PedidoCreateView, PedidoUpdateView, PedidoDeleteView,
)

urlpatterns = [
    # URLs para Insumo
    path('insumos/', InsumoListView.as_view(), name='insumo_list'),
    path('insumos/<int:pk>/', InsumoDetailView.as_view(), name='insumo_detail'),
    path('insumos/nuevo/', InsumoCreateView.as_view(), name='insumo_create'),
    path('insumos/<int:pk>/editar/', InsumoUpdateView.as_view(), name='insumo_update'),
    path('insumos/<int:pk>/eliminar/', InsumoDeleteView.as_view(), name='insumo_delete'),

    # URLs para Proveedor
    path('proveedores/', ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedores/<int:pk>/', ProveedorDetailView.as_view(), name='proveedor_detail'),
    path('proveedores/nuevo/', ProveedorCreateView.as_view(), name='proveedor_create'),
    path('proveedores/<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('proveedores/<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedor_delete'),

    # URLs para Pedido
    path('pedidos/', PedidoListView.as_view(), name='pedido_list'),
    path('pedidos/<int:pk>/', PedidoDetailView.as_view(), name='pedido_detail'),
    path('pedidos/nuevo/', PedidoCreateView.as_view(), name='pedido_create'),
    path('pedidos/<int:pk>/editar/', PedidoUpdateView.as_view(), name='pedido_update'),
    path('pedidos/<int:pk>/eliminar/', PedidoDeleteView.as_view(), name='pedido_delete'),
]

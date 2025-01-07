from django.urls import path
from .views import (
    InsumoListView, InsumoDetailView, InsumoCreateView, InsumoUpdateView, InsumoDeleteView,
    PedidoListView,
    ProveedorListView,
)

urlpatterns = [
    # URLs para Insumo
    path('insumos/', InsumoListView.as_view(), name='insumo_list'),
    path('insumos/<int:pk>/', InsumoDetailView.as_view(), name='insumo_detail'),
    path('insumos/nuevo/', InsumoCreateView.as_view(), name='insumo_create'),
    path('insumos/<int:pk>/editar/', InsumoUpdateView.as_view(), name='insumo_update'),
    path('insumos/<int:pk>/eliminar/', InsumoDeleteView.as_view(), name='insumo_delete'),

    # URLs para Pedido
    path('pedidos/', PedidoListView.as_view(), name='pedido_list'),

    # URLs para Proveedor
    path('proveedores/', ProveedorListView.as_view(), name='proveedor_list'),
]

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # Ruta raíz, carga Principal.html
    path('', TemplateView.as_view(template_name="Principal.html"), name="principal"),

    # Ruta para Inventario.html
    path('inventario/', TemplateView.as_view(template_name="Inventario.html"), name="inventario"),
]

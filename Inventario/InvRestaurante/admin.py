from django.contrib import admin
from .models import (Insumo, Inventario, Alerta, Administrador, ReporteConsumo,
                     ReporteBodega, Bodega, Historial, Proveedor, Pedido,
                     Categoria, Usuario, Producto, Persona, Operacion)

# Registra los modelos en el panel de administrador
admin.site.register(Insumo)
admin.site.register(Inventario)
admin.site.register(Alerta)
admin.site.register(Administrador)
admin.site.register(ReporteConsumo)
admin.site.register(ReporteBodega)
admin.site.register(Bodega)
admin.site.register(Historial)
admin.site.register(Proveedor)
admin.site.register(Pedido)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Persona)
admin.site.register(Operacion)

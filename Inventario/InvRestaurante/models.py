from django.db import models


# Modelo Insumo: Gestiona los insumos en inventario.
class Insumo(models.Model):
    identificador = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    cantidadDisponible = models.IntegerField()
    unidadMedida = models.CharField(max_length=30)
    nivelReorden = models.IntegerField()
    fechaVencimiento = models.DateField()
    precioUnitario = models.FloatField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.identificador} - {self.nombre} ({self.cantidadDisponible} {self.unidadMedida})"


# Modelo Inventario: Almacena los insumos.
class Inventario(models.Model):
    almacenamiento = models.CharField(max_length=200)

    def __str__(self):
        return self.almacenamiento


# Modelo Alerta: Administra alertas de inventario.
class Alerta(models.Model):
    mensaje = models.CharField(max_length=255)
    fecha = models.DateField()
    TIPO_ALERTA_CHOICES = [
        ('bajo_stock', 'Bajo Stock'),
        ('vencimiento', 'Vencimiento'),
    ]
    tipo = models.CharField(max_length=50, choices=TIPO_ALERTA_CHOICES)

    def generarAlerta(self):
        pass

    def enviarNotificacion(self):
        pass


# Modelo Administrador: Administra el inventario.
class Administrador(models.Model):
    revision = models.TextField()
    control = models.TextField()

    def crearReporte(self):
        pass


# Modelo ReporteConsumo: Genera reportes de consumo.
class ReporteConsumo(models.Model):
    tipo = models.CharField(max_length=100)
    periodoInicio = models.DateField()
    periodoFin = models.DateField()
    datos = models.TextField()

    def generarReporte(self):
        pass

    def exportarReporte(self):
        pass


# Modelo ReporteBodega: Administra reportes de bodega.
class ReporteBodega(models.Model):
    datos = models.TextField()
    tipo = models.CharField(max_length=100)

    def generarReporte(self):
        pass

    def actualizarReporte(self):
        pass


# Modelo Bodega: Gestiona las cantidades de productos.
class Bodega(models.Model):
    cantidadUtileria = models.IntegerField()
    cantidadCondimentos = models.IntegerField()
    cantidadVerduras = models.IntegerField()
    cantidadCarnes = models.IntegerField()


# Modelo Historial: Registra cambios en el inventario.
class Historial(models.Model):
    actualizacion = models.TextField()

    def registrarEntrada(self, entrada):
        pass

    def registrarSalida(self, salida):
        pass

    def consultarHistorial(self):
        pass


# Modelo Proveedor: Administra los proveedores.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    contacto = models.CharField(max_length=100)

    def registrarProveedor(self):
        pass

    def consultarProveedores(self):
        pass

    def actualizarProveedor(self):
        pass

    def __str__(self):
        return f"{self.nombre} - {self.contacto}"


# Modelo Pedido: Registra pedidos de clientes.
class Pedido(models.Model):
    cliente = models.CharField(max_length=255)
    fecha = models.DateField()
    ESTADO_PEDIDO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    estado = models.CharField(max_length=50, choices=ESTADO_PEDIDO_CHOICES)

    def realizarPedido(self):
        pass

    def cancelarPedido(self):
        pass

    def __str__(self):
        return f"Pedido de {self.cliente} - {self.estado} ({self.fecha})"


# Modelo Categoria: Clasifica los insumos.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def registrarCategoria(self):
        pass

    def actualizarCategoria(self):
        pass

    def consultarCategorias(self):
        pass

    def __str__(self):
        return self.nombre


# Modelo Usuario: Gestiona a los usuarios del sistema.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    email = models.EmailField()

    def registrarUsuario(self):
        pass

    def actualizarUsuario(self):
        pass

    def consultarUsuarios(self):
        pass

    def __str__(self):
        return self.nombre


# Modelo GestionInventario: Operaciones generales de inventario.
class GestionInventario(models.Model):

    def agregarItem(self, item):
        pass

    def eliminarItem(self, item):
        pass

    def buscarItem(self, nombre):
        pass

    def actualizar(self):
        pass


# Modelo Producto: Información de productos.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()

    def crearPlato(self):
        pass

    def actualizarPlato(self):
        pass

    def calcularCosto(self):
        pass

    def __str__(self):
        return self.nombre


# Modelo Persona: Representa a una persona genérica.
class Persona(models.Model):
    edad = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Modelo Operacion: Detalles de operaciones realizadas.
class Operacion (models.Model):
    fechaRegistro = models.DateTimeField()
    cantidad = models.IntegerField()
    costoTotal = models.FloatField()
    motivoSalida = models.TextField()

    def __str__(self):
        return f"Operación ({self.fechaRegistro}) - {self.cantidad} unidades"

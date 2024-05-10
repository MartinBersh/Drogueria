from entities.Cliente import Cliente
from entities.Empleado import Empleado
from entities.Pedido import Pedido
from entities.Producto import Producto
from entities.Proveedor import Proveedor


class DrogueriaManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.clientes = []
        self.productos = []
        self.pedidos = []
        self.empleados = []
        self.proveedores = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_proveedor(self, proveedor):
        self.proveedores.append(proveedor)


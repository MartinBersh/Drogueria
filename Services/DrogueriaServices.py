from creatorsConfig.DrogueriaManager import DrogueriaManager
from creatorsConfig.ProductosBuilder import ProductoBuilder
from entities.Cliente import Cliente
from entities.Empleado import Empleado
from entities.Pedido import Pedido
from entities.Producto import Producto
from entities.Proveedor import Proveedor


class DrogueriaServices:

    def __init__(self):
        self.productos = []

    def crearProductoBuilder(self):
        productoBuilder = ProductoBuilder("1", "Paracetamol")
        productoBuilder.conDescripcion("Medicamento para aliviar el dolor y la fiebre")
        productoBuilder.conPrecio(5.99)
        productoBuilder.conCantidadEnStock(100)
        productoBuilder.conIdProveedor("1")
        producto = productoBuilder.build()

        print(producto)


    def usoSingleton(self):
        manager = DrogueriaManager()

        cliente1 = Cliente("1", "María", "González", "12345678A", "Calle Principal 123", "987654321")
        manager.agregar_cliente(cliente1)

        producto1 = Producto("1", "Paracetamol", "Medicamento para aliviar el dolor y la fiebre", 5.99, 100, "1")
        manager.agregar_producto(producto1)

        pedido1 = Pedido("1", "2024-05-05", "1", [(producto1.idProducto, 2, producto1.precio)])
        manager.agregar_pedido(pedido1)

        empleado1 = Empleado("1", "Juan", "Arango", "Cajero", "123456789", "Calle Secundaria 456")
        manager.agregar_empleado(empleado1)

        proveedor1 = Proveedor("1", "Cruz verde", "Av.14 #1-17", "987654321", [producto1.idProducto])
        manager.agregar_proveedor(proveedor1)

        print(cliente1)
        print("\n------------------------------------\n")
        print(producto1)
        print("\n------------------------------------\n")
        print(pedido1)
        print("\n------------------------------------\n")
        print(empleado1)
        print("\n------------------------------------\n")
        print(proveedor1)

    def usoPrototype(self):
        prototipo_producto = Producto("2", "Azitromicina", "Medicamento antibiotico", 3.99, 100,
                                      "1")

        nuevo_producto1 = prototipo_producto.clone()
        nuevo_producto1.idProducto = "3"

        nuevo_producto2 = prototipo_producto.clone()
        nuevo_producto2.idProducto = "4"
        nuevo_producto2.precio = 4.50

        print(nuevo_producto1)
        print("\n------------------------------------\n")
        print(nuevo_producto2)

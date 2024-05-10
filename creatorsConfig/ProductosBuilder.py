from entities.Producto import Producto


class ProductoBuilder:
    def __init__(self, idProducto, nombre):
        self.idProducto = idProducto
        self.nombre = nombre
        self.descripcion = ""
        self.precio = 0.0
        self.cantidad_en_stock = 0
        self.idProveedor = ""

    def conDescripcion(self, descripcion):
        self.descripcion = descripcion
        return self

    def conPrecio(self, precio):
        self.precio = precio
        return self

    def conCantidadEnStock(self, cantidad_en_stock):
        self.cantidad_en_stock = cantidad_en_stock
        return self

    def conIdProveedor(self, idProveedor):
        self.idProveedor = idProveedor
        return self

    def build(self):
        return Producto(self.idProducto, self.nombre, self.descripcion,
                        self.precio, self.cantidad_en_stock, self.idProveedor)

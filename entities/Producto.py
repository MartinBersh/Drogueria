import copy


class Producto:
    def __init__(self, idProducto, nombre, descripcion, precio, cantidad_en_stock, idProveedor):
        self.idProducto = idProducto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_en_stock = cantidad_en_stock
        self.idProveedor = idProveedor

    def __str__(self):
        return f"ID Producto: {self.idProducto}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\n" \
               f"Precio: {self.precio}\nCantidad en Stock: {self.cantidad_en_stock}\nID Proveedor: {self.idProveedor}"

    def __copy__(self):
        cls = self.__class__
        new_producto = cls.__new__(cls)
        new_producto.__dict__.update(self.__dict__)
        return new_producto

    def clone(self):
        return copy.copy(self)
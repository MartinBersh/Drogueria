
class Proveedor:

    def __init__(self, idProveedor, nombre, direccion, telefono, productos):
        self.idProveedor = idProveedor
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = productos

    def __str__(self):
        return f"ID Proveedor: {self.idProveedor}\nNombre: {self.nombre}\nDirección: {self.direccion}\n" \
               f"Teléfono: {self.telefono}\nProductos Suministrados: {self.productos}"

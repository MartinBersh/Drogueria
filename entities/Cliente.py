
class Cliente:

    def __init__(self, idCliente, nombre, apellidos, dni, direccion, telefono):
        self.idCliente = idCliente
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"ID Cliente: {self.idCliente}\nNombre: {self.nombre}\nApellidos: {self.apellidos}\nDNI: {self.dni}\nDirección: {self.direccion}\nTeléfono: {self.telefono}"




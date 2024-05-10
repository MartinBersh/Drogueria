class Empleado:
    def __init__(self, idEmpleado, nombre, apellidos, cargo, telefono, direccion):
        self.idEmpleado = idEmpleado
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"ID Empleado: {self.idEmpleado}\nNombre: {self.nombre}\nApellidos: {self.apellidos}\nCargo: {self.cargo}\nTeléfono: {self.telefono}\nDirección: {self.direccion}"






class Pedido:
    def __init__(self, idPedido, fecha, idCliente, detalles_pedido):
        self.idPedido = idPedido
        self.fecha = fecha
        self.idCliente = idCliente
        self.detalles_pedido = detalles_pedido

    def __str__(self):
        return f"ID Pedido: {self.idPedido}\nFecha: {self.fecha}\nID Cliente: {self.idCliente}\nDetalles del Pedido: {self.detalles_pedido}"

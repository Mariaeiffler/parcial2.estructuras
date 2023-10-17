from Habitacion import Habitacion
class Habitacion_Suite (Habitacion):
    def __init__(self, numero, piso, edificio, precio:int, precio_min: int, capacidad:int, banio_priv:bool, balcon:bool):
        super.__init__(numero, piso, edificio)
        self.precio = precio
        self.precio_min = precio_min
        self.capacidad = capacidad
        self.banio_priv = banio_priv
        self.balcon = balcon
from Habitacion import Habitacion

class Habitacion_Suite (Habitacion):
    def __init__(self, numero, piso, edificio, reservas, precio:int, precio_min: int, capacidad:int, banio_priv:bool, balcon:bool):
        super().__init__(numero, piso, edificio, reservas)
        self.precio = precio
        self.precio_min = precio_min
        self.capacidad = capacidad
        self.banio_priv = banio_priv
        self.balcon = balcon
        
    def __str__ (self):
         return ('Habitación: {}, precio:{}, baño privado: {}, balcón: {}'.format (self.numero, self.precio, self.banio_priv, self.balcon))

from Habitacion import Habitacion
class Habitacion_Simple (Habitacion):
    def __init__(self, numero, piso, edificio, reservas, precio:int, precio_min: int, capacidad:int, banio_priv:bool, balcon:bool):
        super().__init__(numero, piso, edificio, reservas)
        self.precio = precio
        self.precio_min = precio_min
        self.capacidad = capacidad
        self.banio_priv = banio_priv
        self.balcon = balcon
    def __str__ (self):
        return ('Habitación: {}, precio:{}, baño privado: {}, balcón: {}'. format (self.numero, self.precio, self.banio_priv, self.balcon))
        
        
#creo habitaciones
def crear_habitaciones_simples():
    h1 = Habitacion_Simple(1,1,1,5000,10000,2,False,False)
    h2 = Habitacion_Simple(2,1,1,10000,10000,2,True,False)
    h3 = Habitacion_Simple(3,1,1,10000,10000,2,False,True)
    h4 = Habitacion_Simple(4,1,1,15000,10000,2,True,True)
    return(h1,h2,h3,h4)

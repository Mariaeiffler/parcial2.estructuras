from Habitacion import Habitacion
class Habitacion_Doble (Habitacion):
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
def crear_habitaciones_dobles():
    h5 = Habitacion_Doble(5,2,1,20000,10000,4,False,False)
    h6 = Habitacion_Doble(6,2,1,25000,10000,4,True,False)
    h7 = Habitacion_Doble(7,2,1,25000,10000,4,False,True)
    h8 = Habitacion_Doble(8,2,1,30000,10000,4,True,True)
    return (h5,h6,h7,h8)
    
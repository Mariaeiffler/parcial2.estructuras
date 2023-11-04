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
        
    
    #creo habitaciones
def crear_habitaciones_suite():
    h9 = Habitacion_Suite(9,2,1,35000,10000,4,False,False)
    h10 = Habitacion_Suite(10,2,1,40000,10000,4,True,False)
    h11 = Habitacion_Suite(11,2,1,40000,10000,4,False,True)
    h12 = Habitacion_Suite(12,2,1,45000,10000,4,True,True)
    return (h9,h10,h11,h12)

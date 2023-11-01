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
        return ('Habitación: {}, precio:{}, baño privado: {}, balcón: {}', format (self.numero, self.precio, self.banio_priv, self.balcon))
        
        
#creo habitaciones
def crear_habitaciones_simples():
    h1 = Habitacion_Simple(1,1,1,5000,10000,2,False,False)
    h2 = Habitacion_Simple(2,1,1,10000,10000,2,True,False)
    h3 = Habitacion_Simple(3,1,1,10000,10000,2,False,True)
    h4 = Habitacion_Simple(4,1,1,15000,10000,2,True,True)
    # h5 = Habitacion_Simple(5,1,1,10000,10000,2,False,False)
    # h6 = Habitacion_Simple(6,1,1,10000,10000,2,False,False)
    # h7 = Habitacion_Simple(7,1,1,10000,10000,2,False,False)
    # h8 = Habitacion_Simple(8,1,1,10000,10000,2,False,False)
    # h9 = Habitacion_Simple(9,1,1,10000,10000,2,False,False)
    # h10 = Habitacion_Simple(10,1,1,10000,10000,2,False,False)
    # h11 = Habitacion_Simple(11,1,1,12000,10000,2,True,False)
    # h12 = Habitacion_Simple(12,1,1,12000,10000,2,True,False)
    # h13 = Habitacion_Simple(13,1,1,12000,10000,2,True,False)
    # h14 = Habitacion_Simple(14,1,1,12000,10000,2,True,False)
    # h15 = Habitacion_Simple(15,1,1,12000,10000,2,True,False)
    # h16 = Habitacion_Simple(16,1,1,12000,10000,2,True,False)
    # h17 = Habitacion_Simple(17,1,1,12000,10000,2,True,False)
    # h18 = Habitacion_Simple(18,1,1,12000,10000,2,True,False)
    # h19 = Habitacion_Simple(19,1,1,12000,10000,2,True,False)
    # h20 = Habitacion_Simple(20,1,1,12000,10000,2,True,False)
    # h21 = Habitacion_Simple(21,1,1,12000,10000,2,True,False)
    # h22 = Habitacion_Simple(22,1,1,15000,10000,2,True,True)
    # h23 = Habitacion_Simple(23,1,1,15000,10000,2,True,True)
    # h24 = Habitacion_Simple(24,1,1,15000,10000,2,True,True)
    # h25 = Habitacion_Simple(25,1,1,15000,10000,2,True,True)
    # h26 = Habitacion_Simple(26,1,1,15000,10000,2,True,True)
    # h27 = Habitacion_Simple(27,1,1,15000,10000,2,True,True)
    # h28 = Habitacion_Simple(28,1,1,15000,10000,2,True,True)
    # h29 = Habitacion_Simple(29,1,1,15000,10000,2,True,True)
    # h30 = Habitacion_Simple(30,1,1,15000,10000,2,True,True)
    # h31 = Habitacion_Simple(31,1,1,15000,10000,2,True,True)
    # h32 = Habitacion_Simple(32,1,1,15000,10000,2,True,True)
    # h33 = Habitacion_Simple(33,1,1,15000,10000,2,True,True)
    # h34 = Habitacion_Simple(34,1,1,15000,10000,2,True,True)
    # h35 = Habitacion_Simple(35,1,1,15000,10000,2,True,True)
    # h36 = Habitacion_Simple(36,1,1,15000,10000,2,True,True)
    # h37 = Habitacion_Simple(37,1,1,15000,10000,2,True,True)
    # h38 = Habitacion_Simple(38,1,1,15000,10000,2,True,True)
    # h39 = Habitacion_Simple(39,1,1,15000,10000,2,True,True)
    # h40 = Habitacion_Simple(40,1,1,15000,10000,2,True,True)
    # h41 = Habitacion_Simple(41,1,1,15000,10000,2,True,True)
    # h42 = Habitacion_Simple(42,1,1,15000,10000,2,True,True)
    # h43 = Habitacion_Simple(43,1,1,15000,10000,2,True,True)
    # h44 = Habitacion_Simple(44,1,1,15000,10000,2,True,True)
    # h45 = Habitacion_Simple(45,1,1,15000,10000,2,True,True)
    # h46 = Habitacion_Simple(46,1,1,15000,10000,2,True,True)
    # h47 = Habitacion_Simple(47,1,1,15000,10000,2,True,True)
    # h48 = Habitacion_Simple(48,1,1,15000,10000,2,True,True)
    # h49 = Habitacion_Simple(49,1,1,15000,10000,2,True,True)
    # h50 = Habitacion_Simple(50,1,1,15000,10000,2,True,True)
    return(h1,h2,h3,h4)

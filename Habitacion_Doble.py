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
    # h55 = Habitacion_Doble(55,2,1,25000,10000,4,True,True)
    # h56 = Habitacion_Doble(56,2,1,25000,10000,4,True,True)
    # h57 = Habitacion_Doble(57,2,1,25000,10000,4,True,True)
    # h58 = Habitacion_Doble(58,2,1,25000,10000,4,True,True)
    # h59 = Habitacion_Doble(59,2,1,25000,10000,4,True,True)
    # h60 = Habitacion_Doble(60,2,1,25000,10000,4,True,True)
    # h61 = Habitacion_Doble(61,2,1,25000,10000,4,True,True)
    # h62 = Habitacion_Doble(62,2,1,25000,10000,4,True,True)
    # h63 = Habitacion_Doble(63,2,1,25000,10000,4,True,True)
    # h64 = Habitacion_Doble(64,2,1,25000,10000,4,True,True)
    # h65 = Habitacion_Doble(65,2,1,25000,10000,4,True,True)
    # h66 = Habitacion_Doble(66,2,1,25000,10000,4,True,True)
    # h67 = Habitacion_Doble(67,2,1,25000,10000,4,True,True)
    # h68 = Habitacion_Doble(68,2,1,25000,10000,4,True,True)
    # h69 = Habitacion_Doble(69,2,1,25000,10000,4,True,True)
    # h70 = Habitacion_Doble(70,2,1,25000,10000,4,True,True)
    # h71 = Habitacion_Doble(71,2,1,25000,10000,4,True,True)
    # h72 = Habitacion_Doble(72,2,1,25000,10000,4,True,True)
    # h73 = Habitacion_Doble(73,2,1,25000,10000,4,True,True)
    # h74 = Habitacion_Doble(74,2,1,25000,10000,4,True,True)
    # h75 = Habitacion_Doble(75,2,1,25000,10000,4,True,True)
    # h76 = Habitacion_Doble(76,2,1,25000,10000,4,True,True)
    # h77 = Habitacion_Doble(77,2,1,25000,10000,4,True,True)
    # h78 = Habitacion_Doble(78,2,1,25000,10000,4,True,True)
    # h79 = Habitacion_Doble(79,2,1,25000,10000,4,True,True)
    # h80 = Habitacion_Doble(80,2,1,25000,10000,4,True,True)
    # h81 = Habitacion_Doble(81,2,1,25000,10000,4,True,True)
    # h82 = Habitacion_Doble(82,2,1,25000,10000,4,True,True)
    # h83 = Habitacion_Doble(83,2,1,25000,10000,4,True,True)
    # h84 = Habitacion_Doble(84,2,1,25000,10000,4,True,True)
    # h85 = Habitacion_Doble(85,2,1,25000,10000,4,True,True)
    # h86 = Habitacion_Doble(86,2,1,25000,10000,4,True,True)
    # h87 = Habitacion_Doble(87,2,1,25000,10000,4,True,True)
    # h88 = Habitacion_Doble(88,2,1,25000,10000,4,True,True)
    # h89 = Habitacion_Doble(89,2,1,25000,10000,4,True,True)
    # h90 = Habitacion_Doble(90,2,1,25000,10000,4,True,True)
    # h91 = Habitacion_Doble(91,2,1,25000,10000,4,True,True)
    # h92 = Habitacion_Doble(92,2,1,25000,10000,4,True,True)
    # h93 = Habitacion_Doble(93,2,1,25000,10000,4,True,True)
    # h94 = Habitacion_Doble(94,2,1,25000,10000,4,True,True)
    # h95 = Habitacion_Doble(95,2,1,25000,10000,4,True,True)
    # h96 = Habitacion_Doble(96,2,1,25000,10000,4,True,True)
    # h97 = Habitacion_Doble(97,2,1,25000,10000,4,True,True)
    # h98 = Habitacion_Doble(98,2,1,25000,10000,4,True,True)
    # h99 = Habitacion_Doble(99,2,1,25000,10000,4,True,True)
    # h100 = Habitacion_Doble(100,2,1,25000,10000,4,True,True)
    return (h5,h6,h7,h8)
    
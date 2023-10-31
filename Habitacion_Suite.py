from Habitacion import Habitacion
class Habitacion_Suite (Habitacion):
    def __init__(self, numero, piso, edificio, precio:int, precio_min: int, capacidad:int, banio_priv:bool, balcon:bool):
        super().__init__(numero, piso, edificio)
        self.precio = precio
        self.precio_min = precio_min
        self.capacidad = capacidad
        self.banio_priv = banio_priv
        self.balcon = balcon
        
    
    #creo habitaciones
def crear_habitaciones_suite():
    h9 = Habitacion_Suite(9,2,1,35000,10000,4,False,False)
    h10 = Habitacion_Suite(10,2,1,40000,10000,4,True,False)
    h11 = Habitacion_Suite(11,2,1,40000,10000,4,False,True)
    h12 = Habitacion_Suite(12,2,1,45000,10000,4,True,True)
    # h105 = Habitacion_Suite(105,2,1,35000,10000,4,True,True)
    # h106 = Habitacion_Suite(106,2,1,35000,10000,4,True,True)
    # h107 = Habitacion_Suite(107,2,1,35000,10000,4,True,True)
    # h108 = Habitacion_Suite(108,2,1,35000,10000,4,True,True)
    # h109 = Habitacion_Suite(109,2,1,35000,10000,4,True,True)
    # h110 = Habitacion_Suite(110,2,1,35000,10000,4,True,True)
    # h111 = Habitacion_Suite(111,2,1,35000,10000,4,True,True)
    # h112 = Habitacion_Suite(112,2,1,35000,10000,4,True,True)
    # h113 = Habitacion_Suite(113,2,1,35000,10000,4,True,True)
    # h114 = Habitacion_Suite(114,2,1,35000,10000,4,True,True)
    # h115 = Habitacion_Suite(115,2,1,35000,10000,4,True,True)
    # h116 = Habitacion_Suite(116,2,1,35000,10000,4,True,True)
    # h117 = Habitacion_Suite(117,2,1,35000,10000,4,True,True)
    # h118 = Habitacion_Suite(118,2,1,35000,10000,4,True,True)
    # h119 = Habitacion_Suite(119,2,1,35000,10000,4,True,True)
    # h120 = Habitacion_Suite(120,2,1,35000,10000,4,True,True)
    # h121 = Habitacion_Suite(121,2,1,35000,10000,4,True,True)
    # h122 = Habitacion_Suite(122,2,1,35000,10000,4,True,True)
    # h123 = Habitacion_Suite(123,2,1,35000,10000,4,True,True)
    # h124 = Habitacion_Suite(124,2,1,35000,10000,4,True,True)
    # h125 = Habitacion_Suite(125,2,1,35000,10000,4,True,True)
    # h126 = Habitacion_Suite(126,2,1,35000,10000,4,True,True)
    # h127 = Habitacion_Suite(127,2,1,35000,10000,4,True,True)
    # h128 = Habitacion_Suite(128,2,1,35000,10000,4,True,True)
    # h129 = Habitacion_Suite(129,2,1,35000,10000,4,True,True)
    # h130 = Habitacion_Suite(130,2,1,35000,10000,4,True,True)
    # h131 = Habitacion_Suite(131,2,1,35000,10000,4,True,True)
    # h132 = Habitacion_Suite(132,2,1,35000,10000,4,True,True)
    # h133 = Habitacion_Suite(133,2,1,35000,10000,4,True,True)
    # h134 = Habitacion_Suite(134,2,1,35000,10000,4,True,True)
    # h135 = Habitacion_Suite(135,2,1,35000,10000,4,True,True)
    # h136 = Habitacion_Suite(136,2,1,35000,10000,4,True,True)
    # h137 = Habitacion_Suite(137,2,1,35000,10000,4,True,True)
    # h138 = Habitacion_Suite(138,2,1,35000,10000,4,True,True)
    # h139 = Habitacion_Suite(139,2,1,35000,10000,4,True,True)
    # h140 = Habitacion_Suite(140,2,1,35000,10000,4,True,True)
    # h141 = Habitacion_Suite(141,2,1,35000,10000,4,True,True)
    # h142 = Habitacion_Suite(142,2,1,35000,10000,4,True,True)
    # h143 = Habitacion_Suite(143,2,1,35000,10000,4,True,True)
    # h144 = Habitacion_Suite(144,2,1,35000,10000,4,True,True)
    # h145 = Habitacion_Suite(145,2,1,35000,10000,4,True,True)
    # h146 = Habitacion_Suite(146,2,1,35000,10000,4,True,True)
    # h147 = Habitacion_Suite(147,2,1,35000,10000,4,True,True)
    # h148 = Habitacion_Suite(148,2,1,35000,10000,4,True,True)
    # h149 = Habitacion_Suite(149,2,1,35000,10000,4,True,True)
    # h150 = Habitacion_Suite(150,2,1,35000,10000,4,True,True)
    return (h9,h10,h11,h12)

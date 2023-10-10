class Habitacion ():
    def __init__(self, numero:int , piso:int , edificio):
        self.numero = numero
        self.piso = piso
        self.edificio = edificio
        
    def __str__ (self):
        return ('Habitación: {}, piso: {}, edificio {}', format (self.numero, self.piso, self.edificio))
    
    def ocupar (self):
        return
        
    def desocupar (self):
        return
    
    
class Habitacion_Simple (Habitacion):
    def __init__(self, numero, piso, edificio, precio:int, precio_min: int, capacidad:int, banio_priv:bool, balcon:bool):
        super.__init__(numero, piso, edificio)
        self.precio = precio
        self.precio_min = precio_min
        self.capacidad = capacidad
        self.banio_priv = banio_priv
        self.balcon = balcon
        
        
class Habitacion_Doble (Habitacion):
    def __init__(self, numero, piso, edificio, precio:int, precio_min: int, capacidad:int, banio_priv:bool, balcon:bool):
        super.__init__(numero, piso, edificio)
        self.precio = precio
        self.precio_min = precio_min
        self.capacidad = capacidad
        self.banio_priv = banio_priv
        self.balcon = balcon
        
class Habitacion_Suite (Habitacion):
    def __init__(self, numero, piso, edificio, precio:int, precio_min: int, capacidad:int, banio_priv:bool, balcon:bool):
        super.__init__(numero, piso, edificio)
        self.precio = precio
        self.precio_min = precio_min
        self.capacidad = capacidad
        self.banio_priv = banio_priv
        self.balcon = balcon
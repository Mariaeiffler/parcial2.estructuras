class Habitacion ():
    def __init__(self, numero:int , piso:int , edificio, reservas = []):
        self.numero = numero
        self.piso = piso
        self.edificio = edificio
        self.reservas = reservas
        
    #def __str__ (self):
    #     return ('Habitación: {}, piso: {}, edificio {}', format (self.numero, self.piso, self.edificio))
    
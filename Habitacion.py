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
    

        

        

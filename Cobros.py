from datetime import *

class Cobro():
    def __init__(self, monto, usuario, descripcion, fecha = datetime.today()):
        self.monto = monto
        self.usuario = usuario
        self.descripcion = descripcion
        self.fecha = fecha
        
    def __str__(self):
        return('El monto es {}, el usuario {} ha reservado la habitacion {}'.format(self.monto, self.usuario.usuario, self.descripcion.numero))
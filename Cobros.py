from datetime import *
from Habitacion import Habitacion
from Buffet import Comida

class Cobro():
    def __init__(self, monto, usuario, descripcion, fecha = datetime.today()):
        self.monto = monto
        self.usuario = usuario
        self.descripcion = descripcion
        self.fecha = fecha
        
    def __str__(self):
        if isinstance(self.descripcion, Habitacion):
            return('El monto es {}, el usuario {} ha reservado la habitacion {}'.format(self.monto, self.usuario.usuario, self.descripcion.numero))
        elif isinstance(self.descripcion, Comida):
            return('El usuario {} ha pedido {}'.format(self.usuario.usuario, self.descripcion))
        else:
            return('El monto es {}, el usuario {} cambió su habitación a la numero {}'.format(self.monto, self.usuario.usuario, self.descripcion))
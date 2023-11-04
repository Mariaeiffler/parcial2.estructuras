from datetime import *

class Cobro():
    def __init__(self, monto, usuario, descripcion, fecha = datetime.today()):
        self.monto = monto
        self.usurio = usuario
        self.descripcion = descripcion
        self.fecha = fecha
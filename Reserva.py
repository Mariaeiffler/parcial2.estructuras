from datetime import *

class Reserva():
    def __init__(self, numero, usuario, fecha_inicio, fecha_finalizacion, habitacion, fecha):
        self.numero = numero
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.habitacion = habitacion
        self.fecha = fecha
        
    def __str__(self):
        return('Su numero de reserva es {}, ha reservado la habitacion numero {} en las fechas {} - {} '.format(self.numero, self.habitacion, self.fecha_inicio.strftime('%d/%m/%Y'), self.fecha_finalizacion.strftime('%d/%m/%Y')))
    

from Persona import Persona
from prueba_menu import *

class Cliente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,tipo='nivel 1', reservas = []):
        super().__init__(nombre,dni,direccion,contacto,fecha_nac,mail)
        self.usuario = usuario
        self.contrasena = contrasena
        self.tipo=tipo
        self.reservas= reservas
    
    def realizar_reserva(self, lista):
        habitacion=validacion_preg_hab()
        print('La habitación que usted ha seleccionado es {}'.format())#hacer q se printee el str d la habitacion
        fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
        fecha_inicio = convertirfecha_datetime(fecha_inicio)
        fecha_fin = input('Ingrese la fecha de finalización de su estadía de su estadía en el formato dd/mm/aaaa ')
        fecha_fin = convertirfecha_datetime(fecha_fin)
        fecha_inicio, fecha_fin = comparacion_fechas(fecha_inicio, fecha_fin)
        for habitacion in lista:
            if habitacion.numero == habitacion:
                # hay q hacer que vaya comparando las fechas que estan en reservas d las habitaciones

        return (self.usuario, fecha_inicio, fecha_fin, habitacion)
    

    
    # def realizar_pedido():
        
        
        
    #def tipo(self):
        #verificar que tipo de cliente es en base a sus gastos
        
    #def historial_reservas(self):
    
    #def realizar_pedido_buffet():
    
    #def __str__(self):
    
    #def tipocliente(self)
    
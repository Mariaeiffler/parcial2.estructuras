from Persona import Persona
from prueba_menu import *

class Cliente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,soy_empleado,contrasena,tipo='nivel 1', reservas = []):
        super().__init__(nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado)
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
                if len(habitacion.reservas) == 0:
                    fechas = [fecha_inicio,fecha_fin]
                    habitacion.reservas.append(fechas)
                else:
                    validacion = True
                    for estadia in habitacion.reservas:
                        if (estadia[0]<fecha_inicio and estadia[1]<fecha_fin) or (estadia[0]>fecha_inicio and estadia[1]>fecha_fin):
                            pass
                        else:
                            validacion = False
                        #hay q ver q pasa el dia d check out d alguien es el dia d check in d otro
                    if validacion == True:
                        fechas = [fecha_inicio,fecha_fin]
                        habitacion.reservas.append(fechas)
                        self.reservas.append(fechas)
                        #hay q ver el tema d los gastos xq aca tambien habria que agregar ese costo
        return (fecha_inicio, fecha_fin, habitacion)
    

    
    # def realizar_pedido():
        
        
        
    #def tipo(self):
        #verificar que tipo de cliente es en base a sus gastos
        
    #def historial_reservas(self):
    
    #def realizar_pedido_buffet():
    
    #def __str__(self):
    
    #def tipocliente(self)
    
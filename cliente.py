from Persona import Persona
from prueba_menu import reserva


class Cliente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,tipo='nivel 1', reservas = []):
        super().__init__(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena)
        self.tipo=tipo
        self.reservas= reservas
    
    def realizar_reserva(self, lista, diccionario:dict):
        fecha_inicio, fecha_fin, habitacion = reserva()
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
                        num_reserva = len(diccionario)+1
                        print('Su reserva se realizó con exito en las fechas {} - {} y su numero de reserva es '.format(fecha_inicio,fecha_fin,num_reserva))
                        #hay q ver el tema d los gastos xq aca tambien habria que agregar ese costo
                    else:
                        preg = input('En las fechas ingresadas la habitación seleccionada ya esta ocupada \n Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n')
                        # preg = val_res(preg)
                        # if preg == 1:
                            
        return (num_reserva, fecha_inicio, fecha_fin, habitacion)
    
    # def modificar_reserva(self, lista):
    #     fecha = input('Introduzca el día que realizó la reserva en el formato dd/mm/aaaa')
    #     fecha = convertirfecha_datetime(fecha)
        
        

    
    # def realizar_pedido():
        
        
        
    #def tipo(self):
        #verificar que tipo de cliente es en base a sus gastos
        
    #def historial_reservas(self):
    
    #def realizar_pedido_buffet():
    
    #def __str__(self):
    
    #def tipocliente(self)
    
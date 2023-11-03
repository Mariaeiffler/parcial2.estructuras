from Persona import Persona
from prueba_menu import reserva
from prueba_menu import val_numres
from prueba_menu import val_preg_mod
from prueba_menu import val_res


class Cliente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,tipo='nivel 1', reservas = []):
        super().__init__(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena)
        self.tipo=tipo
        self.reservas= reservas
    
    def realizar_reserva(self, lista, diccionario:dict):
        fecha_inicio, fecha_fin, hab = reserva()
        print(fecha_inicio)
        for habitacion in lista:
            if habitacion.numero == int(hab):
                if len(habitacion.reservas) == 0:
                    fechas = [fecha_inicio,fecha_fin]
                    habitacion.reservas.append(fechas)
                    num_reserva = len(diccionario)+1
                    print('Su reserva se realizó con exito en las fechas {} - {} y su numero de reserva es {}'.format(fecha_inicio,fecha_fin,num_reserva))
                    #quiero q se imprima sin la hora como hago?
                else:
                    validacion = True
                    while validacion:
                        for estadia in habitacion.reservas:
                            if (estadia[0]<fecha_inicio and estadia[1]<fecha_fin) or (estadia[0]>fecha_inicio and estadia[1]>fecha_fin):
                                pass
                            else:
                                fechas = [fecha_inicio,fecha_fin]
                                habitacion.reservas.append(fechas)
                                print(habitacion.reservas)
                                self.reservas.append(fechas)
                                num_reserva = len(diccionario)+1
                                print('Su reserva se realizó con exito en las fechas {} - {} y su numero de reserva es {}'.format(fecha_inicio,fecha_fin,num_reserva))
                                validacion = False
                            #hay q ver q pasa el dia d check out d alguien es el dia d check in d otro
                        preg = input('En las fechas ingresadas la habitación seleccionada ya esta ocupada \n Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas')
                        preg = val_res(preg)
                        # HAY QUE VER COMO LO QUEREMOS HACER, SI QUEREMOS QUE TENGA QUE PONER TODO DEVUELTA O PUEDA ELEGIR COMO EN EL INPUT
                        # TAMBIEN LE PODRÍAMOS IMPRIMIR EN QUE FECHAS ESTÁ OCUPADA LA HABITACION QUE SELECCIÓ COMO PARA QUE PUEDA ELEGIR otra
            
        return (num_reserva, fecha_inicio, fecha_fin, habitacion)
    
    def modificar_reserva(self, reservas:dict, habitaciones):
        numres = input('Ingrese su numero de reserva  ')
        numres = val_numres(numres, reservas, self.usuario)
        preg=input('Elija una opcion: \n 1. Modificar las fechas \n 2. Mofificar la habitación \n')
        preg=val_preg_mod(preg)
        seguir = True
        reserva = reservas.get(numres)
        numhab = reserva.habitacion
        print(numhab)
        for hab in habitaciones:
            print(hab.numero)
            if hab.numero == numhab:
                res = hab.reservas
                #no entiendo porque no funciona
                print(res)
        while seguir:
            if preg == 1:
                print('La habitación seleccionada está ocupada en las fechas: \n {}'.format(res))
        return
                #que printee las fechas y le pregunte que fecha quiere modificiar
                #tambien tiene q poder modificar la habitacion que reservo
    
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
    
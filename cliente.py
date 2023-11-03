from Persona import Persona
from prueba_menu import reserva
from prueba_menu import val_numres
from prueba_menu import val_opc
from prueba_menu import convertirfecha_datetime
from prueba_menu import hab_ocupada
from prueba_menu import comparacion_fechas
from prueba_menu import validacion_preg_hab
from prueba_menu import modi_hab


class Cliente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,tipo='nivel 1', reservas = []):
        super().__init__(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena)
        self.tipo=tipo
        self.reservas= reservas
    
    def realizar_reserva(self, lista, diccionario:dict):
        fecha_inicio, fecha_fin, hab = reserva()
        val = hab_ocupada(fecha_inicio, fecha_fin, hab, lista)
        while (val==False):
            preg = input('Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n')
            imprimir = 'Error. Elija una opcion: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n'
            preg = val_opc(preg, 1, 3, imprimir)
            val, fecha_inicio, fecha_fin, hab = modi_hab(val, preg, fecha_inicio, fecha_fin, hab, lista)  
        for habitacion in lista:
            if habitacion.numero == int(hab):
                fechas = [fecha_inicio,fecha_fin]
                habitacion.reservas.append(fechas)
                num_reserva = len(diccionario)+1
                print('Su reserva se realizó con exito en las fechas {} - {} y su numero de reserva es {}. \n Recuerde que el horario de check in es desde las 15:00 hs y el check out hasta las 12:00 hs'.format(fecha_inicio.strftime('%d/%m/%Y'),fecha_fin.strftime('%d/%m/%Y'),num_reserva))     
        return (num_reserva, fecha_inicio, fecha_fin, habitacion)
    
    def modificar_reserva(self, reservas:dict, lista):
        numres = input('Ingrese su numero de reserva  ')
        numres = val_numres(numres, reservas, self.usuario)
        reserva = reservas.get(numres)
        hab = reserva.habitacion
        print(reserva)
        preg = input('Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n')
        imprimir = 'Error. Elija una opcion: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n'
        preg = val_opc(preg, 1, 3, imprimir)
        val = True
        while val == False:
            if preg == 1:
                fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
                fecha_inicio = convertirfecha_datetime(fecha_inicio)
                fecha_inicio, fecha_fin = comparacion_fechas(fecha_inicio)
                val = hab_ocupada(fecha_inicio, fecha_fin, hab, lista)
            if preg == 2:
                hab=validacion_preg_hab()
                val = hab_ocupada(fecha_inicio, fecha_fin, hab, lista)
            if preg == 3:
                fecha_inicio, fecha_fin, hab = reserva()
                val = hab_ocupada(fecha_inicio, fecha_fin, hab, lista)       
        for hab in lista:
            print(hab.numero)
            if hab.numero == hab:
                res = hab.reservas
                #no entiendo porque no funciona
                print(res)

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
    
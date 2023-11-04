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
        while val==False:
            preg = input('Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n')
            imprimir = 'Error. Elija una opcion: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n'
            preg = val_opc(preg, 1, 3, imprimir)
            val, fecha_inicio, fecha_fin, hab = modi_hab(val, preg, fecha_inicio, fecha_fin, hab, lista)  
        for habitacion in lista:
            if habitacion.numero == int(hab):
                habitacion.reservas.append([fecha_inicio,fecha_fin])
                num_reserva = len(diccionario)+1
                # falta lo d cobros
                self.reservas.append([fecha_inicio,fecha_fin])
                print(self.reservas)
                print('Su reserva se realizó con exito en las fechas {} - {} y su numero de reserva es {}. \n Recuerde que el horario de check in es desde las 15:00 hs y el check out hasta las 12:00 hs'.format(fecha_inicio.strftime('%d/%m/%Y'),fecha_fin.strftime('%d/%m/%Y'),num_reserva))     
        return num_reserva, fecha_inicio, fecha_fin, int(hab)
    
    def modificar_reserva(self, reservas:dict, lista):
        numres = input('Ingrese su numero de reserva  ')
        numres = val_numres(numres, reservas, self.usuario)
        reserva = reservas.get(numres)
        print(reserva)
        val = False
        print(self.reservas)
        while val == False:
            preg = input('Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n')
            imprimir = 'Error. Elija una opcion: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n'
            preg = val_opc(preg, 1, 3, imprimir)
            for habitacion in lista:
                if int(reserva.habitacion) == int(habitacion.numero):
                    self.reservas.remove([reserva.fecha_inicio, reserva.fecha_finalizacion])
                    habitacion.reservas.remove([reserva.fecha_inicio, reserva.fecha_finalizacion])
                    val, fecha_inicio, fecha_fin, hab = modi_hab(val, preg, reserva.fecha_inicio, reserva.fecha_finalizacion, reserva.habitacion, lista)
                    reserva.fecha_inicio = fecha_inicio
                    reserva.fecha_finalizacion = fecha_fin
                    reserva.habitacion = hab
                    self.reservas.append([reserva.fecha_inicio, reserva.fecha_finalizacion])
                    break
            for habitacion in lista:
                if int(habitacion.numero) == int(hab):    
                    habitacion.reservas.append([fecha_inicio, fecha_fin])
                    print('Su reserva se modificó con exito. {}'.format(reserva))
        return
    
    def cancelar_reserva(self,reservas:dict, lista):
        numres = input('Ingrese su numero de reserva  ')
        numres = val_numres(numres, reservas, self.usuario)
        reserva = reservas.get(numres)
        print(reserva)
        preg = input('¿Desea cancelar su reserva definitivamente? \n 1. Si \2. No \n')
        imprimir = 'Error. ¿Desea cancelar su reserva definitivamente? \n 1. Si \n 2. No \n'
        preg = val_opc(preg, 1, 2, imprimir)
        if preg == 1:
            reservas.pop(numres)
            self.reservas.remove([reserva.fecha_inicio, reserva.fecha_finalizacion])
            for habitacion in lista:
                if int(reserva.habitacion) == int(habitacion.numero):
                    habitacion.reservas.remove([reserva.fecha_inicio, reserva.fecha_finalizacion])
        # hace falta borrar el objeto?
        return
                    
                    
            
        
        

    
    # def realizar_pedido():
        
        
        
    #def tipo(self):
        #verificar que tipo de cliente es en base a sus gastos
        
    #def historial_reservas(self):
    
    #def realizar_pedido_buffet():
    
    #def __str__(self):
    
    #def tipocliente(self)
    
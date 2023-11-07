from Persona import Persona
from Validaciones import *
from Funciones import *


class Cliente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,tipo='nivel 1', reservas = []):
        super().__init__(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena)
        self.tipo=tipo
        self.reservas= reservas
        
    def __str__(self):
        if len(self.reservas) != 0:
            res_imp = ''
            for res in self.reservas:
                res_imp += res[0].strftime('%d/%m/%Y') + ' - ' + res[1].strftime('%d/%m/%Y') + '   '
            return('El cliente de nombre {} y dni {} es de {} y sus reservas son: {}'.format(self.nombre, self.dni, self.tipo, res_imp))
        else:
            return('El clientes de nombre {} y dni {} no tiene reservas en el hotel'.format(self.nombre, self.dni))
    
    def realizar_reserva(self, lista, diccionario:dict):
        ''' Esta funcion le permite al usuario llevar a cabo la reserva. Se le pedirá al mismo las 
        fechas en las cuales desea realizar su reserva. En caso de que la fecha seleccionada no este 
        disponible se le mostraran las fechas en las cuales esta ocupada para que seleccione una opcion
        valida. En caso de que ingrese una fecha de salida que no sea coherente con la de entrada, 
        se le preguntará si desea cambiar la fecha, la habitacion o ambas'''
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
                numres = len(diccionario)+1
                while(valPalabraDic (numres,diccionario)):
                    numres = numres+1
                # falta lo d cobros
                self.reservas.append([fecha_inicio,fecha_fin])
        return numres, fecha_inicio, fecha_fin, int(hab)
    
    def modificar_reserva(self, reservas:dict, lista):
        ''' Esta funcion le permite al usuario poder cambiar su reserva, ya sea la modificacion de la fecha, habitacion o ambas'''
        print('Recuerde que si hace una modificacion de su reserva, no se le reembolsará la diferencia de precio en caso de hacerla \n pero si se le cobrará en caso de que la seleccionada tenga un valor mayor')
        seguir = volver_atras()
        if seguir == False:
            return None
        else:
            numres = input('Ingrese su numero de reserva  ')
            numres = val_numres(numres, reservas, self.usuario)
            reserva = reservas.get(numres)
            print(reserva)
            val = False
            while val == False:
                preg = input('Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n')
                imprimir = 'Error. Elija una opcion: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n'
                preg = val_opc(preg, 1, 3, imprimir)
                for habitacion in lista:
                    if int(reserva.habitacion) == int(habitacion.numero):
                        hab_ant = habitacion
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
                        dif_precio = habitacion.precio - hab_ant.precio
                        
                    # ver como hacemos esto
                        print('Su reserva se modificó con exito. {}'.format(reserva))
            return
    
    def cancelar_reserva(self,reservas:dict, lista):
        ''' Esta funcion le permite al usuario cancelar la reserva definitivamente'''
        numres = input('Ingrese su numero de reserva o escriba "volver" si desea volver al menú principal \n')
        if numres == 'volver':
            return None
        else:
            numres = val_numres(numres, reservas, self.usuario)
        reserva = reservas.get(numres)
        print(reserva)
        preg = input('¿Desea cancelar su reserva definitivamente? \n 1. Si \n 2. No \n')
        imprimir = 'Error. ¿Desea cancelar su reserva definitivamente? \n 1. Si \n 2. No \n'
        preg = val_opc(preg, 1, 2, imprimir)
        if preg == 1:
            reservas.pop(numres)
            self.reservas.remove([reserva.fecha_inicio, reserva.fecha_finalizacion])
            for habitacion in lista:
                if int(reserva.habitacion) == int(habitacion.numero):
                    habitacion.reservas.remove([reserva.fecha_inicio, reserva.fecha_finalizacion])
                    print('Su reserva se ha cancelado con exito ')
        else:
            print('Se ha cancelado la cancelación de su reserva')
        return
    
    def asignar_nivel(self, vector):
        '''Esta funcion permite asignarle un nivel al cliente en funcion a los gastos hechos en la totalidad de sus estadias en el hotel'''
        gastos = 0
        for cobro in vector:
            if cobro.usuario.usuario == self.usuario:
                gastos += cobro.monto
        if gastos <= 50000:
            self.tipo = 'nivel 1'
        elif gastos >= 100000:
            self.tipo = 'nivel 3'
        else:
            self.tipo = 'nivel 2'
        return
    
 
        
                
    
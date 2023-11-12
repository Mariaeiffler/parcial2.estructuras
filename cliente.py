from Persona import Persona
from Funciones import *
from Cobros import Cobro
from Reserva import Reserva
from Cola import Cola


class Cliente(Persona):
    def __init__(self,nombre,usuario,dni,contacto,fecha_nac,mail,contrasena,tipo='nivel 1', reservas = []):
        super().__init__(nombre,usuario,dni,contacto,fecha_nac,mail,contrasena)
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
    
    def realizar_reserva(self, habitaciones, reservas:dict, cobros):
        ''' Esta funcion le permite al usuario llevar a cabo la reserva. Se le pedirá al mismo las 
        fechas en las cuales desea realizar su reserva. En caso de que la fecha seleccionada no este 
        disponible se le mostraran las fechas en las cuales esta ocupada para que seleccione una opcion
        valida. En caso de que ingrese una fecha de salida que no sea coherente con la de entrada, 
        se le preguntará si desea cambiar la fecha, la habitacion o ambas'''
        fecha_inicio, fecha_fin, hab = reserva()
        val = hab_ocupada(fecha_inicio, fecha_fin, hab, habitaciones)
        while val==False:
            preg = input('Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n')
            imprimir = 'Error. Elija una opcion: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n'
            preg = val_opc(preg, 1, 3, imprimir)
            val, fecha_inicio, fecha_fin, hab = modi_hab(val, preg, fecha_inicio, fecha_fin, hab, habitaciones)  
        for habitacion in habitaciones:
            if habitacion.numero == int(hab):
                objhab = habitacion
                habitacion.reservas.append([fecha_inicio,fecha_fin])
                numres = len(reservas)+1
                while(valPalabraDic (numres,reservas)):
                    numres = numres+1
                self.reservas.append([fecha_inicio,fecha_fin])
                
        reserva1=Reserva(numres,self, fecha_inicio, fecha_fin, int(hab), datetime.today())
        reservas[numres]=reserva1
        monto,objhab=obtener_precio(habitaciones, int(hab))
        cobro = Cobro(monto,self,objhab)
        print(cobro)
        cobros = agregar_cobro(cobros, cobro)
        print(cobros)
        self.asignar_nivel(cobros)
        
        print('Su reserva se realizó con exito en las fechas {} - {} y su numero de reserva es {}. \n Recuerde que el horario de check in es desde las 15:00 hs y el check out hasta las 12:00 hs'.format(fecha_inicio.strftime('%d/%m/%Y'),fecha_fin.strftime('%d/%m/%Y'),numres))
        return cobros
    
    def modificar_reserva(self, reservas:dict, lista, cobros):
        ''' Esta funcion le permite al usuario poder cambiar su reserva, ya sea la modificacion de la fecha, habitacion o ambas'''
        print('Recuerde que si hace una modificacion de su reserva, no se le reembolsará la diferencia de precio en caso de haberla \n pero si se le cobrará en caso de que la seleccionada tenga un valor mayor')
        seguir = volver_atras()
        if seguir:
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
                        habi = habitacion
                        habitacion.reservas.append([fecha_inicio, fecha_fin])
                        dif_precio = habitacion.precio - hab_ant.precio                        
                        if dif_precio > 0:
                            print('Su reserva se modificó con exito. {}. La diferencia de precio es {}'.format(reserva, dif_precio))
                        else:
                            print('Su reserva se modificó con exito. {}'.format(reserva, dif_precio))
            if dif_precio > 0:
                cobro = Cobro(dif_precio,self,hab)
                cobros = agregar_cobro(cobros, cobro)
        else:
            pass      
        return cobros 
                     
    
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
    
    def check_in(self):
        res_hoy = False
        for reserva in self.reservas:
            if reserva[0].date() == datetime.now().date(): 
                hora = datetime.now().hour
                res_hoy = True
                if hora > 14:
                    print('Se realizó con éxito su check-in')
                else:
                    print('No se pudo realizar su check-in, recuerde que recién puede hacer el check-in a partir de las 15:00 hs')
        if res_hoy == False:
            print('No se pudo realizar su check-in. El día de hoy no tiene una reserva')
            
    def check_out(self):
        res_hoy = False
        for reserva in self.reservas:
            if reserva[1].date() == datetime.now().date(): 
                hora = datetime.now().hour
                res_hoy = True
                if hora < 11:
                    print('Se realizó con éxito su check-out')
                else:
                    print('Su check-out ya se realizó automaticamente a las 12:00 hs')
        if res_hoy == False:
            print('No se pudo realizar su check-out. El día de hoy no termina una estadía')
            
    def realizarPedidoBuffet (cliente,cola:Cola,buffet,cobros):
        monto, comida = hacer_pedido(buffet)
        tareabuffet=comida.descripcion
        cola.encolar(tareabuffet)
        cobro = Cobro(monto, cliente, comida)
        cobros = agregar_cobro(cobros, cobro)
        cliente.asignar_nivel(cobros)
        print('Su pedido se realizó con éxito ')
        return cobros
        
        
           
    
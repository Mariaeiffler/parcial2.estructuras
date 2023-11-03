from Persona import Persona
from prueba_menu import reserva
from prueba_menu import val_numres
from prueba_menu import val_preg_mod
from prueba_menu import convertirfecha_datetime
from prueba_menu import hab_ocupada
from prueba_menu import comparacion_fechas
from prueba_menu import validacion_preg_hab


class Cliente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,tipo='nivel 1', reservas = []):
        super().__init__(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena)
        self.tipo=tipo
        self.reservas= reservas
    
    def realizar_reserva(self, lista, diccionario:dict):
        fecha_inicio, fecha_fin, hab = reserva()
        val = hab_ocupada(fecha_inicio, fecha_fin, hab, lista)
    #hay q ver q pasa el dia d check out d alguien es el dia d check in d otro
        while (val==False):
            print('En las fechas ingresadas la habitación seleccionada ya está ocupada. Acá puede ser la ocupación de la misma:')
            for habitacion in lista:
                for res in habitacion.reservas:
                    print(res[0].strftime('%d/%m/%Y'), '-', res[1].strftime('%d/%m/%Y')) 
            preg = input('Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n')
            preg = val_preg_mod(preg)
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
        for habitacion in lista:
            if habitacion.numero == int(hab):
                fechas = [fecha_inicio,fecha_fin]
                habitacion.reservas.append(fechas)
                num_reserva = len(diccionario)+1
                print('Su reserva se realizó con exito en las fechas {} - {} y su numero de reserva es {}'.format(fecha_inicio.strftime('%d/%m/%Y'),fecha_fin.strftime('%d/%m/%Y'),num_reserva))     
        return (num_reserva, fecha_inicio, fecha_fin, habitacion)
    
    def modificar_reserva(self, reservas:dict, habitaciones):
        numres = input('Ingrese su numero de reserva  ')
        numres = val_numres(numres, reservas, self.usuario)
        reserva = reservas.get(numres)
        numhab = reserva.habitacion
        print(numhab)
        preg = input('Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n 3. Elegir una nueva habitación y otras fechas \n')
        preg = val_preg_mod(preg)
        seguir = True

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
    
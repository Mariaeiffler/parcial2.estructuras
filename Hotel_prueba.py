import pickle
from Personal import Personal
from cliente import Cliente
from Persona import Persona # creo q no hace falta
from Habitacion_Doble import *
from Habitacion_Simple import *
from Habitacion_Suite import *
from Tareas_Empleados import tareas_empleados 
from Funciones import *
from Reserva import Reserva
from datetime import *
from Cobros import Cobro
from nodo import NodoTarea # creo q no hace falta
from list_enlazada import Lista_Enlazada # creo q no hace falta
from Buffet import Comida
import numpy as np
from Estadisticas import *
from Gerente import Gerente
from Cola import Cola


class Hotel():
    def __init__(self,nombre,contrasena_ing_personal='personal123'):
        self.nombre=nombre
        self.empleados=dict()
        self.clientes=dict()
        self.contrasena_ing_personal=contrasena_ing_personal
        self.tareas=tareas_empleados 
        self.habitaciones = [habitacion for habitacion in crearHab()]
        self.reservas=dict()
        self.bajasEmpleados=set()
        self.cobros = np.array([])
        self.buffet=crear_buffet(Comida.crear_comidas())
        self.pedidosBuffet=Cola()
        
    def entrar(self):
        '''Esta funcion permite que se ejecute el programa. Dependiendo de si el usuario es un cliente, empleado o genente, se le permiten realizar distintas operaciones'''
        obtener_pickle(self, 'abrir')
    
        seguir = True 
        gerente=Gerente('Fransisco','gerente',"10101010",'obelisco','5491100000000','06/11/2003','gerente@gmail.com','Gerente1','gerente')
        self.empleados[gerente.usuario]=gerente
        self.tareas['gerente']['empleados'].append(gerente.usuario)
        
        while seguir==True: #Fijarnos si queremos poner el while aca o en alguna otra parte del programa
            pregunta=input(('Elija una de las siguientes opciones: \n 1. Sign up (si es un cliente) \n 2. Sign in \n'))
            imprimir = 'Error. Elija una de las siguientes opciones: \n 1. Sign up \n 2. Sign in \n'
            pregunta=val_opc(pregunta,1,2,imprimir)
            
            match pregunta:
                # registro del cliente:
                case 1:
                    nombre,usuario,dni,contacto,fecha_nac,mail,contrasena = infoPersonas (self.clientes,self.empleados)
                    cliente=Cliente(nombre,usuario,dni,contacto,fecha_nac,mail,contrasena,'nivel 1',[])
                    self.clientes[usuario]=cliente
                    print('Su usuario se ha creado con exito. Si desea seguir en el programa ingrese sesión. ')
                    #agregar q tambien pueda salir
                
                # inicio de sesion
                case 2:
                    usuario, contrasena = valSignIn (self.clientes, self.empleados)
                    cliente,empleado,tipo = valTipoUsuario(usuario,self.clientes,self.empleados)
                    
                    # menu cliente
                    if cliente:
                        pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n')
                        imprimir='Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n'
                        pregcliente=val_opc(pregcliente,1,7,imprimir)
                        cliente = self.clientes.get(usuario)
                        while pregcliente != 7:
                            match pregcliente:
                            # hacer una reserva
                                case 1:
                                    num_reserva,fecha_inicio,fecha_fin,habitacion = cliente.realizar_reserva(self.habitaciones, self.reservas)
                                    reserva=Reserva(num_reserva,self.clientes.get(usuario), fecha_inicio, fecha_fin, habitacion, datetime.today())
                                    self.reservas[num_reserva]=reserva
                                    monto,objhab=obtener_precio(self.habitaciones, habitacion)
                                    cobro = Cobro(monto,self.clientes.get(usuario),objhab)
                                    self.cobros = agregar_cobro(self.cobros, cobro)
                                    cliente.asignar_nivel(self.cobros)
                                    print('Su reserva se realizó con exito en las fechas {} - {} y su numero de reserva es {}. \n Recuerde que el horario de check in es desde las 15:00 hs y el check out hasta las 12:00 hs'.format(fecha_inicio.strftime('%d/%m/%Y'),fecha_fin.strftime('%d/%m/%Y'),num_reserva))
                                    
                                # pedir algo en el buffet
                                case 2:
                                    monto, comida = hacer_pedido(self.buffet)
                                    tareabuffet=comida.descripcion
                                    self.pedidosBuffet.encolar(tareabuffet)
                                    cobro = Cobro(monto, cliente, comida)
                                    self.cobros = agregar_cobro(self.cobros, cobro)
                                    cliente.asignar_nivel(self.cobros)
                                    print('Su pedido se realizó con éxito ')
                                
                                # modificar una reserva
                                case 3:
                                    print('Recuerde que si hace una modificacion de su reserva, no se le reembolsará la diferencia de precio en caso de hacerla \n pero si se le cobrará en caso de que la seleccionada tenga un valor mayor')
                                    seguir = volver_atras()
                                    if seguir:
                                        dif_precio, hab = cliente.modificar_reserva(self.reservas, self.habitaciones, self.cobros)
                                        if dif_precio > 0:
                                            cobro = Cobro(dif_precio,cliente,hab)
                                            self.cobros = agregar_cobro(self.cobros, cobro)
                                    else:
                                        pass
                                    
                                #cancelar una reserva
                                case 4:
                                    if cliente.cancelar_reserva(self.reservas, self.habitaciones) == None:
                                        pass
                                    
                                case 5:
                                    cliente.check_in()
                                    
                                case 6:
                                    cliente.check_out()
                                    
                            pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n')
                            imprimir='Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n'
                            pregcliente=val_opc(pregcliente,1,7,imprimir)
                        
                        seguir = False #ponerlo afuera del while asi tmb se hace para el gerente, pero ver como funciona
                        
                    else:
                        
                        # menu gerente
                        if tipo=='gerente': #si cambiamos algo del menu del gerente cambiar el rango de las validaciones y los dos str.
                            pregGerente=input('Elija una de las siguientes opciones: \n 1. Crear un empleado \n 2. Dar de baja un empleado \n 3. Inventario del personal \n 4. Ver estadísticas \n 5. Nomina de Clientes \n 6. Asignación de Tareas \n 7. Historial de baja de empleados \n 8. Historial de Reservas \n 9. Cerrar Sesión \n')
                            imprimir='Error. Elija una de las siguientes opciones: \n 1. Crear un empleado \n 2. Dar de baja un empleado \n 3. Inventario del personal \n 4. Ver estadísticas \n 5. Nomina de Clientes \n 6. Asignación de Tareas \n 7. Historial de baja de empleados \n 8. Historial de Reservas \n 9. Cerrar Sesión \n '
                            pregGerente=val_opc(pregGerente,1,9,imprimir)
                            gerente=self.empleados.get(usuario)
                            while pregGerente!=9:
                                match pregGerente:
                                    case 1:
                                        #Crear empleado
                                        nombre,usuario,dni,contacto,fecha_nac,mail,contrasena = infoPersonas (self.clientes,self.empleados)
                                        llaves=list(self.tareas.keys())
                                        tipo=input('Ingrese el tipo al que pertenecera el empleado {}: \n'.format(llaves))
                                        tipo=valTipoEmpleado(tipo,self.tareas)
                                        empleado=Personal(nombre,usuario,dni,contacto,fecha_nac,mail,contrasena,tipo)
                                        self.empleados[empleado.usuario]=empleado
                                        self.tareas[tipo]['empleados'].append(empleado.usuario)
                                        print ('El empleado se a creado con éxito.')
                                        
                                    case 2:
                                        #Dar de baja un empleado
                                        usuarioBaja=input('Ingrese el usuario del empleado que desea dar de baja: ')
                                        usuarioBaja=valExiUsu(usuarioBaja,self.empleados)
                                        empleado=self.empleados.get(usuarioBaja)
                                        Personal.bajas(empleado)
                                        self.tareas[empleado.tipo]['empleados'].remove(empleado.usuario)
                                        self.empleados.pop(empleado.usuario)
                                        self.bajasEmpleados.add(empleado)
                                        print('El empleado ha sido eliminado con éxito')
                                        
                                    case 3:
                                        #Inventario de personal
                                        gerente.inv_empleados(self.empleados)
                                            
                                    case 4:
                                        #Estadisticas
                                        gerente.obtener_estadisticas(self.habitaciones, self.cobros)
                                    
                                    case 5:
                                        #Nomina de clientes
                                        gerente.nomina_clientes(self.clientes)
                                    
                                    case 6:
                                        #Asignar una Tarea
                                        gerente.asignarTarea(self.tareas,self.empleados)
                                    
                                    case 7:
                                        #Historial de baja de un empleados
                                        gerente.historialBajasEmpleados(self.bajasEmpleados)
                                    
                                    case 8:
                                        #Historial de reservas
                                        gerente.historial_reservas(self.reservas)
                                        
                                pregGerente=input('\n Elija una de las siguientes opciones: \n 1. Crear un empleado \n 2. Dar de baja un empleado \n 3. Inventario del personal \n 4. Ver estadísticas \n 5. Nomina de Clientes \n 6. Asignar Tarea \n 7. Historial de baja de empleados \n 8. Historial de Reservas \n 9. Cerrar Sesión \n')
                                pregGerente=val_opc(pregGerente,1,9,imprimir)   
    
                            seguir = False #ponerlo afuera del while asi tmb se hace para el gerente, pero ver como funciona
                                
                        #menu empleados
                        else:
                            pregEmpleado=input('\n Ingrese una de las siguientes opciones: \n 1. Realizar una Tarea \n 2. Registrar ingreso \n 3. Registrar egreso \n 4. Visualizar la última tarea realizada \n 5. Cerrar sesión \n') #Agregar el resto de las cosas que debería hacer un empleado
                            imprimir1='\n Error. Ingrese una de las siguientes opciones: \n 1. Realizar una Tarea \n 2. Registrar ingreso \n 3. Registrar egreso \n 4. Visualizar la última tarea realizada \n 5. Cerrar sesión \n'
                            pregEmpleado=val_opc(pregEmpleado,1,5,imprimir1) #Hay que cambiar el rango a medida que agregamos las cosas que hace el empleado
                            personal:Personal=self.empleados.get(usuario)
                            while pregEmpleado!=5: #tmb cambiar acá el máximo
                                match pregEmpleado:
                                    case 1:
                                        #Realizar una tarea
                                        personal.realizarTareas(self.pedidosBuffet)
                                        pass       
                                    
                                    case 2:
                                        #Registar ingreso
                                        personal.registrar_ingreso()
                                        print('Su ingreso se ha registrado con exito')
                                    
                                    case 3:
                                        #Registrar egreso
                                        personal.registrar_egreso()
                                    
                                    case 4:
                                        #Ver la última tarea realizada
                                        personal.visualizarTareaAnterior()
                                        
                                pregEmpleado=input('\n Ingrese una de las siguientes opciones: \n 1. Realizar una Tarea \n 2. Registrar ingreso \n 3. Registrar egreso \n 4. Visualizar la última tarea realizada \n 5. Cerrar sesión \n') #Agregar el resto de las cosas que debería hacer un empleado
                                imprimir1='\n Error. Elija una de las siguientes opciones: \n 1. Realizar una Tarea \n 2. Registrar ingreso \n 3. Registrar egreso \n 4. Visualizar la última tarea realizada \n 5. Cerrar sesión'
                                pregEmpleado=val_opc(pregEmpleado,1,5,imprimir1)
                                
                            seguir = False
                                
        obtener_pickle(self, 'cerrar')
        # seguir = False #ponerlo afuera del while asi tmb se hace para el gerente, pero ver como funciona
        print('Se ha cerrado la sesión con éxito')
        
if __name__ == "__main__":
    hotel=Hotel('POO')
    hotel.entrar()
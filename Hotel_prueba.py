from Personal import Personal
from cliente import Cliente
from Habitacion_Doble import *
from Habitacion_Simple import *
from Habitacion_Suite import *
from Tareas_Empleados import tareas_empleados 
from Funciones import *
from datetime import *
from Buffet import Comida
import numpy as np
from Estadisticas import *
from Gerente import Gerente
from Cola import Cola

'''El Hotel Patagonia Oasis y Ocio es un objeto de clase Hotel inicializado por el metodo 'entrar'. 
Al entrar al programa se podra elegir iniciar sesión, crear un usuario o abandonar la página.

Si se crea un usuario desde el menu principal, el usuario sera del tipo cliente. Al iniciar sesión, 
podrá hacer el check in o check out del hotel, realizar, modificar o eliminar una reserva, o realizar un pedido al buffet. 

Las reservas de los clientes se almacenan en un diccionario llamado reservas y a su vez, los clientes tienen una lista de listas
con las estadías. Además las habitaciones también tienen una lista de listas con las fechas en las que están ocupadas. La política de 
cobro del hotel no permite realizar reembolsos en caso de una cancelación o una modificación de habitación más barata.
El horario de check-in es desde las 15:00 hs y el de check-out hasta las 12:00 hs. En caso de querer hacer el check-out y que la hora
de ejecución sea más tarde de las 12:00 el mismo se realizará automaticamente.

Hay un gerente preestablecido en el sistema, que se crea la primera vez que se corre el programa. El nombre de usuario del gerente es 
'gerente' y su contrasena es 'Gerente1'. Ingresando con este usuario, se podran realizar todas las acciones que puede realizar un gerente. 
Ya sea dar de alta o de baja un empleado, obtener estadísticas, ver distintos historiales e inventarios, ver la nomina de clientes, asignar 
tareas, realizar tareas y visualizar las tareas que realizo previamente. 

El gerente puede asignar tareas a otros empleados o autoasignarse tareas a él mismo. Estas tareas son registradas y almacenadas en una lista 
enlazada perteneciente a cada empleado del hotel. Al asignar la tarea, el gerente le inserta un valor importancia a la tarea (eligiendo un 
numero del 1 al 3), el cual permite que las mismas se ordenen en la lista y el empleado tenga que realizar la tarea con más importancia. 
Los empleados del tipo cocina tienen además la opcion de realizar las ordenes del buffet (las cuales están almacenadas en una cola, así el
empleado puede realizar las ordenes en el orden que fueron realizadas).

Si se inicia sesión con el usuario de un empleado, el empleado podrá realizar las tareas que tiene asignadas, registrar su ingreso y egreso 
(una vez que llega y se retira del trabajo) o visualizar la última tarea que realizo. 

Una vez que el empleado haya realizado una tarea asignada por el gerente, se guarda el título de esta tarea en una pila, para que no se 
pierdan las tareas realizadas y además para que el empleado pueda ver cual fue la última tarea que realizó.  
  
Una vez que el usuario selecciona la opcion 'Abandonar la página' del menu principal (despues de haber cerrado sesión) , toda la infomarción
que se ingreso al programa es guardada en el pickle. 
'''

class Hotel():
    def __init__(self,nombre):
        self.nombre=nombre
        self.empleados=dict()
        self.clientes=dict()
        self.tareas=tareas_empleados 
        self.habitaciones = [habitacion for habitacion in crearHab()]
        self.reservas=dict()
        self.bajasEmpleados=set()
        self.cobros = np.array([])
        self.buffet=crear_buffet(Comida.crear_comidas())
        self.pedidosBuffet=Cola()
        
        gerente=Gerente('Lionel Messi','gerente',"10101010",'5491100000000','24/06/1987','liomessi@gmail.com','Gerente1','gerente')
        self.empleados[gerente.usuario]=gerente
        self.tareas['gerente']['empleados'].append(gerente.usuario)
        
    def entrar(self):
        '''Esta funcion permite que se ejecute el programa. Dependiendo de si el usuario es un cliente, empleado o genente, se le permiten realizar distintas operaciones'''
        obtener_pickle(self, 'abrir')
        
        seguir = True
        
        pregunta=menuPPL()
        
        while seguir==True: 
        
            match pregunta:
                # registro del cliente:
                case 1:
                    nombre,usuario,dni,contacto,fecha_nac,mail,contrasena = infoPersonas (self.clientes,self.empleados)
                    cliente=Cliente(nombre,usuario,dni,contacto,fecha_nac,mail,contrasena,'nivel 1',[])
                    self.clientes[usuario]=cliente
                    print('Su usuario se ha creado con exito. Si desea seguir en el programa ingrese sesión. ')
                    pregunta=menuPPL()
                
                # inicio de sesion
                case 2:
                    usuario, contrasena = valSignIn (self.clientes, self.empleados)
                    cliente,empleado,tipo = valTipoUsuario(usuario,self.clientes,self.empleados)
                    
                    # menu cliente
                    if cliente:
                        pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n')
                        imprimir='Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n'
                        pregcliente=val_opc(pregcliente,1,7,imprimir)
                        cliente:Cliente = self.clientes.get(usuario)
                        while pregcliente != 7:
                            match pregcliente:
                            # hacer una reserva
                                case 1:
                                    self.cobros = cliente.realizar_reserva(self.habitaciones, self.reservas, self.cobros)
                                    
                                # pedir algo en el buffet
                                case 2:
                                    self.cobros=cliente.realizarPedidoBuffet (self.pedidosBuffet,self.buffet,self.cobros)
                                    
                                case 3:
                                    self.cobros = cliente.modificar_reserva(self.reservas, self.habitaciones, self.cobros)
                                    
                                #cancelar una reserva
                                case 4:
                                    if cliente.cancelar_reserva(self.reservas, self.habitaciones) == None:
                                        pass
                                
                                #check in cliente    
                                case 5:
                                    cliente.check_in()
                                
                                #check out cliente    
                                case 6:
                                    cliente.check_out()
                                    
                            pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n')
                            imprimir='Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Realizar check-in \n 6. Realizar check-out \n 7. Cerrar Sesión \n'
                            pregcliente=val_opc(pregcliente,1,7,imprimir)
                        
                        if pregcliente == 7:
                            pregunta=menuPPL() 
                        
                    else:
                        # menu gerente
                        if tipo=='gerente': 
                            pregGerente=input('\n Elija una de las siguientes opciones: \n 1. Crear un empleado \n 2. Dar de baja un empleado \n 3. Inventario del personal \n 4. Ver estadísticas \n 5. Nomina de Clientes \n 6. Asignar Tarea \n 7. Historial de baja de empleados \n 8. Historial de Reservas \n 9. Realizar una Tarea \n 10. Visualizar la última tarea realizada \n 11. Cerrar Sesión \n')
                            imprimir='Error. Elija una de las siguientes opciones: \n 1. Crear un empleado \n 2. Dar de baja un empleado \n 3. Inventario del personal \n 4. Ver estadísticas \n 5. Nomina de Clientes \n 6. Asignar Tarea \n 7. Historial de baja de empleados \n 8. Historial de Reservas \n 9. Realizar una Tarea \n 10. Visualizar la última tarea realizada \n 11. Cerrar Sesión \n'
                            pregGerente=val_opc(pregGerente,1,11,imprimir)
                            gerente:Gerente=self.empleados.get(usuario)
                            while pregGerente!=11:
                                match pregGerente:
                                    case 1:
                                        #Crear empleado
                                        gerente.crearEmpleado(self.clientes,self.empleados,self.tareas)
                                        
                                    case 2:
                                        #Dar de baja un empleado
                                        gerente.bajaEmpleado(self.empleados,self.tareas,self.bajasEmpleados)
                                        
                                    case 3:
                                        #Inventario de personal
                                        gerente.inv_empleados(self.empleados, self.bajasEmpleados)
                                        print('Puede ver el inventario de los empleados en un archivo de texto.')
                                            
                                    case 4:
                                        #Estadisticas
                                        gerente.obtener_estadisticas(self.habitaciones, self.cobros)
                                        print('Puede ver las estadísticas del hotel en un archivo de texto.')
                                    
                                    case 5:
                                        #Nomina de clientes
                                        gerente.nomina_clientes(self.clientes)
                                        print('Puede ver la nómina de los clientes en un archivo de texto.')
                                    
                                    case 6:
                                        #Asignar una Tarea
                                        gerente.asignarTarea(self.tareas,self.empleados)
                                    
                                    case 7:
                                        #Historial de baja de un empleados
                                        gerente.historialBajasEmpleados(self.bajasEmpleados)
                                        print('Puede ver el historial de bajas de empleados en un archivo de texto')
                                    
                                    case 8:
                                        #Historial de reservas
                                        gerente.historial_reservas(self.reservas)
                                        print('Puede ver el historial de reservas en un archivo de texto.')
                                        
                                    case 9:
                                        #Realizar una Tarea
                                        gerente.realizarTareas(self.pedidosBuffet)
                                    
                                    case 10:
                                        #Ver la última tarea realizada
                                        gerente.visualizarTareaAnterior()
                                        
                                pregGerente=input('\n Elija una de las siguientes opciones: \n 1. Crear un empleado \n 2. Dar de baja un empleado \n 3. Inventario del personal \n 4. Ver estadísticas \n 5. Nomina de Clientes \n 6. Asignar Tarea \n 7. Historial de baja de empleados \n 8. Historial de Reservas \n 9. Realizar una Tarea \n 10. Visualizar la última tarea realizada \n 11. Cerrar Sesión \n')
                                pregGerente=val_opc(pregGerente,1,11,imprimir)   
                                
                            if pregGerente == 11:
                                pregunta=menuPPL()
     
                                
                        #menu empleados
                        else:
                            pregEmpleado=input('\n Ingrese una de las siguientes opciones: \n 1. Realizar una Tarea \n 2. Registrar ingreso \n 3. Registrar egreso \n 4. Visualizar la última tarea realizada \n 5. Cerrar sesión \n')
                            imprimir1='\n Error. Ingrese una de las siguientes opciones: \n 1. Realizar una Tarea \n 2. Registrar ingreso \n 3. Registrar egreso \n 4. Visualizar la última tarea realizada \n 5. Cerrar sesión \n'
                            pregEmpleado=val_opc(pregEmpleado,1,5,imprimir1) 
                            personal:Personal=self.empleados.get(usuario)
                            while pregEmpleado!=5: 
                                match pregEmpleado:
                                    case 1:
                                        #Realizar una tarea
                                        personal.realizarTareas(self.pedidosBuffet)
                                        pass       
                                    
                                    case 2:
                                        #Registar ingreso
                                        personal.registrar_ingreso()
                                        print('Su ingreso se ha registrado con éxito')
                                    
                                    case 3:
                                        #Registrar egreso
                                        personal.registrar_egreso()
                                    
                                    case 4:
                                        #Ver la última tarea realizada
                                        personal.visualizarTareaAnterior()
                                        
                                pregEmpleado=input('\n Ingrese una de las siguientes opciones: \n 1. Realizar una Tarea \n 2. Registrar ingreso \n 3. Registrar egreso \n 4. Visualizar la última tarea realizada \n 5. Cerrar sesión \n') 
                                imprimir1='\n Error. Elija una de las siguientes opciones: \n 1. Realizar una Tarea \n 2. Registrar ingreso \n 3. Registrar egreso \n 4. Visualizar la última tarea realizada \n 5. Cerrar sesión'
                                pregEmpleado=val_opc(pregEmpleado,1,5,imprimir1)
                                
                            if pregEmpleado == 5:
                                pregunta=menuPPL()
                                
                            
                case 3:
                    seguir = False
                    break
                                   
        obtener_pickle(self, 'cerrar')
        print('Se ha cerrado la sesión con éxito.')
        
if __name__ == "__main__":
    hotel=Hotel('POO')
    hotel.entrar()
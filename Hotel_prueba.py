import pickle
from Personal import Personal
from cliente import Cliente
from Persona import Persona
# from validaciones import *
from Abrir_archivo import *
from Habitacion_Doble import *
from Habitacion_Simple import *
from Habitacion_Suite import *
from Tareas_Empleados import tareas_empleados 
from prueba_menu import * #despues si lo seguimos usando cambiarle el nombre
from Reserva import Reserva
from datetime import *
from Cobros import Cobro
from nodo import NodoTarea
from list_enlazada import Lista_Enlazada
#from Buffet import Comida
import numpy as np

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
        self.buffet=dict() #
        self.ingresos_egresos=list() #
        
    def entrar(self):
        try:
            with open ('hotel.pickle','rb') as hpickle:
                info = pickle.load(hpickle)
            self.empledos = info.empleados
            self.clientes = info.clientes
            self.habitaciones = info.habitaciones
            self.reservas = info.reservas
            self.cobros = info.cobros
            self.buffet=info.buffet 
            self.ingresos_egresos=info.ingresos_egresos 
        except FileNotFoundError:
            with open ('hotel.pickle','wb') as hpickle:
                pickle.dump(self,hpickle)
        #podriamos ponerlo en una funcion (no estoy segura)
        
        for cliente in self.clientes:
            print(self.clientes.get(cliente))
        print(self.cobros)
        for i in self.cobros:
            print(i)
        
        seguir = True 
        gerente=Personal('milagros Argibay','miliargibay',"45074984",'obelisco','5491123484825','06/11/2003','mili@','Milia123','gerente')
        self.empleados[gerente.usuario]=gerente
        self.tareas['gerente']['empleados'].append(gerente.usuario)
        
        while seguir==True: #Fijarnos si queremos poner el while aca o en alguna otra parte del programa
            pregunta=input(('Elija una de las siguientes opciones: \n 1. Sign up (si es un cliente) \n 2. Sign in \n')) #crear una opcion para cerrar programa o que lo pueda hacer solo el gerente (tipo metodo cerrar pagina del hotel y ahi se cierre el programa y se guarde el hotel?
            imprimir = 'Error. Elija una de las siguientes opciones: \n 1. Sign up \n 2. Sign in \n'
            pregunta=val_opc(pregunta,1,2,imprimir)
            
            match pregunta:
                # registro del cliente:
                case 1:
                    nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena = infoPersonas (self.clientes,self.empleados)
                    cliente=Cliente(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,'nivel 1',[])
                    self.clientes[usuario]=cliente
                    print('Su usuario se ha creado con exito. Si desea seguir en el programa ingrese sesión. ')
                    #agregar q tambien pueda salir
                
                # inicio de sesion
                case 2:
                    usuario, contrasena = valSignIn (self.clientes, self.empleados)
                    cliente,empleado,tipo = valTipoUsuario(usuario,self.clientes,self.empleados) #para hacer el match case y probar (NO OLVIDARSE)
                    
                    # menu cliente
                    if cliente:
                        pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Cerrar Sesión \n')
                        imprimir='Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Cerrar Sesión \n'
                        pregcliente=val_opc(pregcliente,1,5,imprimir)
                        while pregcliente != 5:
                            
                            # hacer una reserva
                            if pregcliente == 1:
                                num_reserva,fecha_inicio,fecha_fin,habitacion=Cliente.realizar_reserva(self.clientes.get(usuario), self.habitaciones, self.reservas)
                                reserva=Reserva(num_reserva,self.clientes.get(usuario), fecha_inicio, fecha_fin, habitacion, datetime.today())
                                self.reservas[num_reserva]=reserva
                                monto,objhab=obtener_precio(self.habitaciones, habitacion)
                                cobro = Cobro(monto,self.clientes.get(usuario),objhab)
                                self.cobros = agregar_cobro(self.cobros, cobro)
                                Cliente.asignar_nivel(self.clientes.get(usuario), self.cobros)
                                print(self.clientes.get(usuario))
                            # hay que ver si queremos crear un diccionario o algo asi con todos los cobros
                                print('Su reserva se realizó con exito en las fechas {} - {} y su numero de reserva es {}. \n Recuerde que el horario de check in es desde las 15:00 hs y el check out hasta las 12:00 hs'.format(fecha_inicio.strftime('%d/%m/%Y'),fecha_fin.strftime('%d/%m/%Y'),num_reserva))
                                
                            # pedir algo en el buffet
                            if pregcliente == 2:
                                # buffet
                                pass
                            
                            # modificar una reserva
                            if pregcliente == 3:
                                Cliente.modificar_reserva(self.clientes.get(usuario), self.reservas, self.habitaciones)
                                
                            #cancelar una reserva
                            if pregcliente == 4:
                                Cliente.cancelar_reserva(self.clientes.get(usuario),self.reservas, self.habitaciones)
                                
                            pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Cerrar Sesión \n')
                            imprimir='Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Cerrar Sesión \n'
                            pregcliente=val_opc(pregcliente,1,5,imprimir)
                            
                        # se cierra el programa y se carga todo a pickle
                        with open ('hotel.pickle','wb') as hpickle:
                            pickle.dump(self,hpickle)
                        seguir = False #ponerlo afuera del while asi tmb se hace para el gerente, pero ver como funciona
                        print('Se ha cerrado la sesión con éxito')
                        
                    else:
                        
                        # menu gerente
                        if tipo=='gerente': #si cambiamos algo del menu del gerente cambiar el rango de las validaciones y los dos str.
                            pregGerente=input('Elija una de las siguientes opciones: \n 1. Crear un empleado \n 2. Dar de baja un empleado \n 3. Inventario del personal \n 4. Ver estadísticas \n 5. Nomina de Clientes \n 6. Asignación de Tareas \n 7. Historial de baja de empleados \n 8. Historial de Reservas \n 9. Cerrar Sesión \n')
                            imprimir='Error. Elija una de las siguientes opciones: \n 1. Crear un empleado \n 2. Dar de baja un empleado \n 3. Inventario del personal \n 4. Ver estadísticas \n 5. Nomina de Clientes \n 6. Asignación de Tareas \n 7. Historial de baja de empleados \n 8. Historial de Reservas \n 9. Cerrar Sesión \n '
                            pregGerente=val_opc(pregGerente,1,9,imprimir)
                            while pregGerente!=9:
                                match pregGerente:
                                    
                                    case 1:
                                        #Crear empleado
                                        nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena = infoPersonas (self.clientes,self.empleados)
                                        llaves=list(self.tareas.keys())
                                        tipo=input('Ingrese el tipo al que pertenecera el empleado {}: \n'.format(llaves))
                                        tipo=valTipoEmpleado(tipo,self.tareas)
                                        empleado=Personal(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,tipo)
                                        self.empleados[empleado.usuario]=empleado
                                        self.tareas[tipo]['empleados'].append(empleado.usuario)
                                        print ('El empleado se a creado con éxito.')
                                        self.ingresos_egresos.append([]) #
                                        
                                    case 2:
                                        #Dar de baja un empleado
                                        usuarioBaja=input('Ingrese el usuario del empleado que desea dar de baja: ')
                                        usuarioBaja=valExiUsu(usuarioBaja,self.empleados)
                                        empleado=self.empleados.get(usuarioBaja)
                                        empleado.bajas()
                                        self.tareas[empleado.tipo]['empleados'].remove(empleado.usuario)
                                        self.empleados.pop(empleado.usuario)
                                        self.bajasEmpleados.add(empleado) #chequear que se haya guardado correctamente
                                        print('El empleado ha sido eliminado con éxito')
                                        
                                    case 3:
                                        #Inventario de personal
                                        print('Los empleados activos son: ')
                                        for clave in self.empleados:
                                            if self.empleados.get(clave).fecbaja == None:
                                                print(self.empleados.get(clave))
                                        print('Los empleados dados de baja son: ')
                                        for clave in self.empleados:
                                            if self.empleados.get(clave).fecbaja != None:
                                                print(self.empleados.get(clave))
                                            
                                    case 4:
                                        #Estadisticas 
                                        pass
                                    
                                    case 5:
                                        print('Los clientes del hotel son: ')
                                        for cliente in self.clientes:
                                            print(self.clientes.get(cliente))
                                    
                                    case 6:
                                        #Asignar una Tarea
                                        llaves=list(self.tareas.keys())
                                        tipo=input('{} \n Ingrese el tipo de personal al que le quiere asignar una tarea: '.format(llaves))
                                        tipo=valTipoEmpleado(tipo,self.tareas)
                                        for i, tarea in enumerate (self.tareas[tipo]['tareas']):
                                            print (F"{i} - {tarea}")
                                        imprimir1='Ingrese la tarea que desea asignar: '
                                        opcionAsignar=input(imprimir1)
                                        opcionAsignar=valOpcAsignacion(opcionAsignar,self.tareas,tipo,'tareas',imprimir1)
                                        for i, empleados in enumerate (self.tareas[tipo]['empleados']):
                                            print (F"{i} - {empleados}")
                                        imprimir2= 'Ingrese el número del usuario del empleados al que le desea asignar la tarea: '
                                        empleadoAsignar=input(imprimir2)
                                        empleadoAsignar=valOpcAsignacion(empleadoAsignar,self.tareas,tipo,'empleados',imprimir2)
                                        imprimir3='Error. Ingrese como nivel de importancia 1, 2 o 3 (siendo 1 el más urgente): '
                                        pregImportancia=input('Niveles de importancia: 1,2,3 (siendo 1 el más urgente). \n Ingrese la importancia de la tarea a realizar: ')
                                        importancia=val_opc(pregImportancia,1,3,imprimir3)
                                        nodoNuevo=NodoTarea(opcionAsignar,importancia)
                                        persona=self.empleados.get(empleadoAsignar)
                                        persona.tareasPendientes.agregarNodoTarea(nodoNuevo)
                                        print('La nueva tarea se ha asignado con éxito.')
                                        print(persona.tareasPendientes.__str__())
                                        pass
                                    
                                    case 7:
                                        #Historial de baja de un empleados
                                        pass
                                    
                                    case 8:
                                        #Historial de reservas
                                        pass
                                    
                                    case 9:
                                        #cerrar sesión
                                        pass
                                        
                                pregGerente=input('Elija una de las siguientes opciones: \n 1. Crear un empleado \n 2. Dar de baja un empleado \n 3. Inventario del personal \n 4. Ver estadísticas \n 5. Nomina de Clientes \n 6. Asignar Tarea \n 7. Historial de baja de empleados \n 8. Historial de Reservas \n 9. Cerrar Sesión \n')
                                pregGerente=val_opc(pregGerente,1,9,imprimir)    
                                        
                        # menu empleado
                        # else:
                        #     #cliente
                        #     pass
                
    # def obtener_inventario_empleados(self):
    #     empleado:Personal
    #     for key, empleado in self.empleados.item():
    #         print(key, empleado.tipo)
            
    # def nomina_clientes(self):
    #     cliente: Cliente
    #     for key, cliente in self.clientes.item():
    #         print(key, cliente.tipo)

        
        
if __name__ == "__main__":
    hotel=Hotel('POO')
    hotel.entrar()
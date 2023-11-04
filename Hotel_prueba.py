from Personal import Personal
from cliente import Cliente
from Persona import Persona
# from Persona import Persona
# from validaciones import *
from Abrir_archivo import *
from Habitacion_Doble import *
from Habitacion_Simple import *
from Habitacion_Suite import *
import pickle
from Tareas_Empleados import tareas_empleados 
from prueba_menu import * #despues si lo seguimos usando cambiarle el nombre
from Reserva import Reserva
from datetime import *

class Hotel():
    def __init__(self,nombre,contrasena_ing_personal='personal123'):
        self.nombre=nombre
        self.empleados=dict()
        self.clientes=dict()
        self.contrasena_ing_personal=contrasena_ing_personal
        self.tareas=tareas_empleados #fijarse si esta bien llamado
        self.habitaciones = [habitacion for habitacion in crearHab()]
        self.reservas=dict()
        
    def entrar(self):
        try:
            with open ('hotel.pickle','rb') as hpickle:
                info = pickle.load(hpickle)
            self.empledos = info.empleados
            self.clientes = info.clientes
            self.habitaciones = info.habitaciones
            self.reservas = info.reservas
        except FileNotFoundError:
            with open ('hotel.pickle','wb') as hpickle:
                pickle.dump(self,hpickle)
        #podriamos ponerlo en una funcion (no estoy segura)
        seguir = True 
        while seguir==True: #Fijarnos si queremos poner el while aca o en alguna otra parte del programa
            pregunta=input(('Elija una de las siguientes opciones: \n 1. Sign up (si es un cliente) \n 2. Sign in \n')) #crear una opcion para cerrar programa o que lo pueda hacer solo el gerente (tipo metodo cerrar pagina del hotel y ahi se cierre el programa y se guarde el hotel?
            imprimir = 'Error. Elija una de las siguientes opciones: \n 1. Sign up \n 2. Sign in \n'
            pregunta=val_opc(pregunta,1,2,imprimir)
            match pregunta:
                case 1:
                    nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena = infoPersonas (self.clientes,self.empleados)
                    cliente=Cliente(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,'nivel 1',[])
                    self.clientes[usuario]=cliente
                    print('Su usuario se ha creado con exito. Si desea seguir en el programa ingrese sesión. ')
                case 2:
                    usuario, contrasena = valSignIn (self.clientes, self.empleados)
                    cliente,empleado,tipo = valTipoUsuario(usuario,self.clientes,self.empleados) #para hacer el match case y probar (NO OLVIDARSE)
                    if cliente:
                        pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Cerrar Sesión \n')
                        imprimir='Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Cerrar Sesión \n'
                        pregcliente=val_opc(pregcliente,1,5,imprimir)
                        while pregcliente != 5:
                            if pregcliente == 1:
                                num_reserva,fecha_inicio,fecha_fin,habitacion=Cliente.realizar_reserva(self.clientes.get(usuario), self.habitaciones, self.reservas)
                                reserva=Reserva(num_reserva,self.clientes.get(usuario), fecha_inicio, fecha_fin, habitacion, datetime.today())
                                self.reservas[num_reserva]=reserva
                                self.clientes[usuario].reservas.append(reserva)
                            if pregcliente == 2:
                                # buffet
                                pass
                            if pregcliente == 3:
                                Cliente.modificar_reserva(self.clientes.get(usuario), self.reservas, self.habitaciones)
                            if pregcliente == 4:
                                # cancelar reserva
                                pass
                            pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Cerrar Sesión \n')
                            imprimir='Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Cerrar Sesión \n'
                            pregcliente=val_opc(pregcliente,1,5,imprimir)
                        with open ('hotel.pickle','wb') as hpickle:
                            pickle.dump(self,hpickle)
                        seguir = False #ponerlo afuera del while asi tmb se hace para el gerente, pero ver como funciona
                        print('Se ha cerrado la sesión con éxito')
                    else:
                        if tipo=='gerente': #si cambiamos algo del menu del gerente cambiar el rango de las validaciones y los dos str.
                            pregGerente=input('Elija una de las siguientes opciones: \n 1. Crear un empleado \n 2. Dar de baja un empleado \n 3. Inventario del personal \n 4. Ver estadísticas \n 5. Nomina de Clientes \n 6. Asignar Tarea \n 7. Historial de baja de empleados \n 8. Historial de Reservas \n 9. Cerrar Sesión \n')
                            imprimir='Error. Elija una de las siguientes opciones: \n 1. Crear un empleado \n 2. Dar de baja un empleado \n 3. Inventario del personal \n 4. Ver estadísticas \n 5. Nomina de Clientes \n 6. Asignar Tarea \n 7. Historial de baja de empleados \n 8. Historial de Reservas \n 9. Cerrar Sesión \n '
                            pregGerente=val_opc(pregGerente,1,9,imprimir)
                            while pregGerente!=9:
                                match pregGerente:
                                    case 1:
                                        #Crear empleado
                                        nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena = infoPersonas (self.clientes,self.empleados)
                                        tipo=input('Ingrese el tipo al que pertenecera el empleado: ')
                                        
                            
                        else:
                            pass
                
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
    
    # habitacion1 = 1
    # fecha1 = 1234
    # fecha2= 1234567
    # for habitacion in hotel.habitaciones:
    #     if habitacion.numero == habitacion1:
    #         print(habitacion.numero)
    #         if len(habitacion.reservas) == 0:
    #             fechas = [fecha1,fecha2]
    #             habitacion.reservas.append(fechas)
    #     print(habitacion.reservas)
    
    # fecha = '30/12/2023'
    # fecha = convertirfecha_datetime(fecha)
    # print(fecha < datetime.today())
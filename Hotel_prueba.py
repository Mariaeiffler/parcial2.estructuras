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
            pregunta=input(('Elija una de las siguientes opciones: \n 1. Sign up (si es un cliente) \n 2.Sign in \n')) #crear una opcion para cerrar programa o que lo pueda hacer solo el gerente (tipo metodo cerrar pagina del hotel y ahi se cierre el programa y se guarde el hotel?
            pregunta=val_opc(pregunta)
            match pregunta:
                case 1:
                    nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena = infoPersonas (self.clientes,self.empleados)
                    cliente=Cliente(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena,'nivel 1',[])
                    self.clientes[usuario]=cliente
                    print('Su usuario se ha creado con exito')
                case 2:
                    usuario, contrasena = valSignIn (self.clientes)
                    pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Cerrar Sesión \n')
                    pregcliente=valiPregCliente(pregcliente)
                    while pregcliente != 5:
                        if pregcliente == 1:
                            num_reserva,fecha_inicio,fecha_fin,habitacion=Cliente.realizar_reserva(self.clientes.get(usuario), self.habitaciones, self.reservas)
                            reserva=Reserva(num_reserva,self.clientes.get(usuario), fecha_inicio, fecha_fin, habitacion, datetime.today())
                            self.reservas[num_reserva]=reserva
                            pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n 5. Cerrar Sesión \n')
                            pregcliente=valiPregCliente(pregcliente)
                        if pregcliente == 2:
                            # buffet
                            pass
                        if pregcliente == 3:
                            Cliente.modificar_reserva(self.clientes.get(usuario), self.reservas, self.habitaciones)
                            pass
                        if pregcliente == 4:
                            # cancelar reserva
                            pass
                        if pregcliente == 5:
                            with open ('hotel.pickle','wb') as hpickle:
                                pickle.dump(self,hpickle)
                            seguir = False
                
    #         case 2:
    #             #validar que exista el usuario y que la contrasena sea correcta
    #             usuario=input('Escriba el nombre de usuario: ')
    #             contrasena=input('Escriba la contrasena: ')
    #             cliente = self.clientes.get(usuario)
    #             if cliente is not None:
    #                 validacion = (contrasena == cliente.contrasena)
    #             else:
    #                 validacion == False
    #             if validacion == False:
    #                 print('El usuario ingresado es incorrecto ')
    #                 usuario=input('Escriba el nombre de usuario: ')
    #                 contrasena=input('Escriba la contrasena: ')
    #                 if cliente is not None:
    #                     validacion = (contrasena == cliente.contrasena)
    #                 else:
    #                     validacion == False
    #                 while(validacion == False):
    #                     print('El usuario ingresado es incorrecto ')
    #                     usuario=input('Escriba el nombre de usuario: ')
    #                     contrasena=input('Escriba la contrasena: ')
    #                     if cliente is not None:
    #                         validacion = (contrasena == cliente.contrasena)
    #                     else:
    #                         validacion == False

                
                
                        
        
    # def save(self): #CHEQUEAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #     with open('hotel.pickle','wb') as f:
    #         pickle.dump(self,f)
            
    # def obtener_inventario_empleados(self):
    #     empleado:Personal
    #     for key, empleado in self.empleados.item():
    #         print(key, empleado.tipo)
            
    # def nomina_clientes(self):
    #     cliente: Cliente
    #     for key, cliente in self.clientes.item():
    #         print(key, cliente.tipo)
    
    # def agregarTareasDicc (self): #comprobar que sea administrador quien agregue la tarea
    #     tipo = input('Ingrese a que tipo de empleado desea agregarle la tarea: ')
    #     while tipo not in tareas_empleados:
    #         tipo = input ('No existe este tipo de empleados, ingrese el tipo de vuelta: ')
    #     tarea= input('Ingrese la tarea que desea agregar: ')
    #     self.tarea_empleado[tipo].append(tarea)
    #     print ('La nueva tarea se ha  agregado con exito.')
    
    # def agregarTipoEmpleado (self):
    #     tipo = input ('ingrese el nuevo tipo de empleado: ')
    #     while tipo in self.tareas_empleado:
    #         tipo = input ('Error, ese tipo de empleado ya existe. Ingrese otro tipo de empleado: ')
    #     tarea = input ('Ingrese una tarea que realizaría este tipo de empleado: ')
    #     self.tareas_empleado[tipo]= tarea
    #     print ('El tipo de empleado fue agregado con exito.')
        
        
if __name__ == "__main__":
    hotel=Hotel('POO')
    print(hotel.habitaciones)
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
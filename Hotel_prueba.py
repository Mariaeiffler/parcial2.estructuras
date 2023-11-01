# from Personal import Personal
# # from cliente import Cliente
# from Persona import Persona
# from validaciones import *
from Abrir_archivo import *
from Habitacion_Doble import *
from Habitacion_Simple import *
from Habitacion_Suite import *
import pickle
from Tareas_Empleados import tareas_empleados 
from prueba_menu import *

class Hotel():
    def __init__(self,nombre,contrasena_ing_personal='personal123'):
        self.nombre=nombre
        self.empleados=dict()
        self.clientes=dict()
        self.contrasena_ing_personal=contrasena_ing_personal
        self.tareas=tareas_empleados #fijarse si esta bien llamado
        self.habitaciones = [habitacion for habitacion in crearHab()]
        
    def entrar(self):
        pregunta=input(('Elija una de las siguientes opciones: \n 1. Sign up (si es un cliente) \n 2.Sign in \n'))
        pregunta=val_opc(pregunta)
        match pregunta:
            case 1:
                #validar que no exista el usuario
                nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena = infoPersonas ()
                existe=valiExiUsu(self.clientes, usuario)
                if existe == False:
                    cliente=Cliente(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,False,contrasena)
                    #mandar info al archivo 
                    self.clientes[usuario]=cliente
                    print('Su usuario se ha creado con exito')
                else:
                    print('Este usuario ya existe, vuelva a registarse o inicie sesión')
                pregcliente=input('Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n')
                pregcliente=valiPregCliente(pregcliente)
                match pregcliente:
                    case 1:
                        habitacion=validacion_preg_hab()
                        print('La habitación que usted ha seleccionado es {}'.format())#hacer q se printee el str d la habitacion
                        #esto lo estoy haciendo en cliente (como metodo)
                
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
    habitacion1 = 1
    for i in hotel.habitaciones:
        if i.numero == habitacion1:
            print(i.reservas)
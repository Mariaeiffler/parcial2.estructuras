from Personal import Personal
from cliente import Cliente
from Persona import Persona
from validaciones import *
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
        self.habitaciones = [habitacion for habitacion in crear_habitaciones_simples()]
        
    def entrar(self):
        pregunta=input(('Elija una de las siguientes opciones: 1. Sign up \n 2.Sign in \n'))
        pregunta=val_opc(pregunta)
        #validacion 
        match pregunta:
            case 1:
                #validar que no exista el usuario
                #validar todos los atributos
                nombre=input('Introduzca su nombre y apellido: ')
                nombre=valNombre2(nombre)
                # en esta validacion no se fija q no tenga espacios? si tiene q poner su nombre y apellido tiene q tener un espacio
                dni=input('Ingrese su DNI:')
                dni=validaciondni(dni)
                direccion=input('Ingrese su direccion:')
                contacto=input('Ingrese su numero de contacto:')
                contacto=validacioncontacto(contacto)
                fecha_nac=input('Ingrese su fecha de nacimiento:')
                fecha_nac=validacionfechanac (fecha_nac)
                mail=input('Ingrese su mail:')
                mail=valMail(mail)
                usuario=input('Escriba el nombre de usuario:')
                usuario=validacionusuario(usuario)
                contrasena=input('Escriba la contrasena:')
                contrasena = validacioncontrasena(contrasena)
                # validacioncontrasena(contrasena) #verificar el nombre de la funcion
                soy_empleado=input('Sos empleado? (responder si o no en minuscula)')
                soy_empleado=validacionempleado(soy_empleado)
                
                if soy_empleado:
                    contrasena_personal=input('Ingrese la contrasena del personal:')
                    while contrasena_personal != self.contrasena_ing_personal:
                        contrasena_personal=input('Ingrese la contrasena del personal:')
                    #validar contrasena personal (definida por nosotras)
                    personal=Personal(nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado)
                    #mandar info a archivo. 
                    #TODO:asignar el tipo de empleado
                    self.empleados[usuario]=personal
                    self.tareas[personal.tipo]['personal'].append(personal)
                else:
                    cliente=Cliente(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,soy_empleado,contrasena)
                    #mandar info al archivo 
                    self.clientes[usuario]=cliente
                    return usuario
    #agregue este return aca xq necesito el usuario para el metodo reservar (no se si hace quilombo con el match)
                
            case 2:
                #validar que exista el usuario y que la contrasena sea correcta
                usuario=input('Escriba el nombre de usuario: ')
                contrasena=input('Escriba la contrasena: ')
                cliente = self.clientes.get(usuario)
                if cliente is not None:
                    validacion = (contrasena == cliente.contrasena)
                else:
                    validacion == False
                if validacion == False:
                    print('El usuario ingresado es incorrecto ')
                    usuario=input('Escriba el nombre de usuario: ')
                    contrasena=input('Escriba la contrasena: ')
                    if cliente is not None:
                        validacion = (contrasena == cliente.contrasena)
                    else:
                        validacion == False
                    while(validacion == False):
                        print('El usuario ingresado es incorrecto ')
                        usuario=input('Escriba el nombre de usuario: ')
                        contrasena=input('Escriba la contrasena: ')
                        if cliente is not None:
                            validacion = (contrasena == cliente.contrasena)
                        else:
                            validacion == False
                
                    
                
                
                        
        
    def save(self): #CHEQUEAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        with open('hotel.pickle','wb') as f:
            pickle.dump(self,f)
            
    def obtener_inventario_empleados(self):
        empleado:Personal
        for key, empleado in self.empleados.item():
            print(key, empleado.tipo)
            
    def nomina_clientes(self):
        cliente: Cliente
        for key, cliente in self.clientes.item():
            print(key, cliente.tipo)
    
    def agregarTareasDicc (self): #comprobar que sea administrador quien agregue la tarea
        tipo = input('Ingrese a que tipo de empleado desea agregarle la tarea: ')
        while tipo not in tareas_empleados:
            tipo = input ('No existe este tipo de empleados, ingrese el tipo de vuelta: ')
        tarea= input('Ingrese la tarea que desea agregar: ')
        self.tarea_empleado[tipo].append(tarea)
        print ('La nueva tarea se ha  agregado con exito.')
    
    def agregarTipoEmpleado (self):
        tipo = input ('ingrese el nuevo tipo de empleado: ')
        while tipo in self.tareas_empleado:
            tipo = input ('Error, ese tipo de empleado ya existe. Ingrese otro tipo de empleado: ')
        tarea = input ('Ingrese una tarea que realizaría este tipo de empleado: ')
        self.tareas_empleado[tipo]= tarea
        print ('El tipo de empleado fue agregado con exito.')
                

            
        
if __name__ == "__main__":
    hotel = Hotel('POO')
    entrar = Hotel.realizar_reserva(hotel)

    #hacer una funcion para mostrar que el hotel esta guardando informacion
    
    


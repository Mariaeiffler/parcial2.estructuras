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
import csv

class Hotel():
    def __init__(self,nombre,contrasena_ing_personal='personal123'):
        self.nombre=nombre
        self.empleados=dict()
        self.clientes=dict()
        self.contrasena_ing_personal=contrasena_ing_personal
        self.tareas=tareas_empleados #fijarse si esta bien llamado
        self.habitaciones = []
        
    # def obtener_habitaciones(self):
    #     try:
    #         with open('Habitaciones.csv', 'r', encoding='utf-8') as archivo:
    #             lector = csv.reader(archivo)                       
    #             for fila in lector:
    #                 for i in fila:
    #                     lista = []
    #                     lista.append(i)
    #                     self.habitaciones.append(lista)
    #     except FileNotFoundError:
    #         with open('Habitaciones.csv', 'w', encoding='utf-8') as archivo_csv:
    #             escritor_csv = csv.writer(archivo_csv)
    #             escritor_csv.writerow(crear_habitaciones_simples())
    #             escritor_csv.writerow(crear_habitaciones_dobles())
    #             escritor_csv.writerow(crear_habitaciones_suite())
    #         #preguntar como hacemos para que se pase bien a la lista
    #     return (self.habitaciones)

        
    def entrar(self):
        pregunta=input(('Elija una de las siguientes opciones: 1. Sign up \n 2.Sign in'))
        pregunta=validacionpregunta(pregunta)
        #validacion 
        match pregunta:
            case 1:
                #validar que no exista el usuario
                #validar todos los atributos
                nombre=input('Introduzca su nombre:')
                nombre=validacionnombre2(nombre)
                dni=input('Ingrese su DNI:')
                dni=validaciondni(dni)
                direccion=input('Ingrese su direccion:')
                contacto=input('Ingrese su numero de contacto:')
                contacto=validacioncontacto(contacto)
                fecha_nac=input('Ingrese su fecha de nacimiento:')
                fecha_nac=validacionfechanac (fecha_nac)
                mail=input('Ingrese su mail:')
                usuario=input('Escriba el nombre de usuario:')
                usuario=validacionusuario(usuario)
                contrasena=input('Escriba la contrasena:')
                contrasena = validacioncontrasena(contrasena)
                validacioncontrasena(contrasena) #verificar el nombre de la funcion
                soy_empleado=input('Sos empleado? (responder si o no en minuscula)')
                soy_empleado=validacionempleado(soy_empleado)
                
                if soy_empleado:
                    contrasena_personal=input('Ingrese la contrasena del personal:')
                    while contrasena_personal != self.contrasena_ing_personal:
                        contrasena_personal=input('Ingrese la contrasena del personal:')
                    #validar contrasena personal (definida por nosotras)
                    personal=Personal(nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado)
                    #mandar info a archivo. 
                    self.empleados[usuario]=personal
                else:
                    cliente=Cliente(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,soy_empleado)
                    #mandar info al archivo 
                    self.clientes[usuario]=cliente
                    return usuario
    #agregue este return aca xq necesito el usuario para el metodo reservar (no se si hace quilombo con el match)
                
            case 2:
                #validar que exista el usuario y que la contrasena sea correcta
                usuario=input('Escriba el nombre de usuario:')
                contrasena=input('Escriba la contrasena:')
                
    def menu (self):
        print ('hola')
        
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
            
    def realizar_reserva(self):
        # usuario = self.entrar()
        # habitaciones = Hotel.obtener_habitaciones(self)
        habitacion = validacion_preg_hab()
        fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
        fecha_inicio = convertirfecha_datetime(fecha_inicio)
        fecha_finalizacion = input('Ingrese la fecha de finaliación de su estadia en el formato dd/mm/aaaa ')
        fecha_finalizacion = convertirfecha_datetime(fecha_finalizacion)
        fecha_inicio, fecha_finalizacion = comparacion_fechas(fecha_inicio, fecha_finalizacion)
        for i in self.habitaciones:
            if i[0]==habitacion:
                print(i[0])
            else:
                print(i[0])

        # self.clientes[usuario].reservas.append(fecha_inicio)
        # self.clientes[usuario].reservas.append(fecha_finalizacion)
        # match pregunta:
        #     case 1:
        return
                

            
        
if __name__ == "__main__":
    hotel = Hotel('POO')
    entrar = Hotel.realizar_reserva(hotel)

    #hacer una funcion para mostrar que el hotel esta guardando informacion
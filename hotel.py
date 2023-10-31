from Personal import Personal
from cliente import Cliente
from Persona import Persona
from validaciones import *
from Abrir_archivo import *
import pickle
class Hotel():
    def __init__(self,nombre,contrasena_ing_personal='personal123'):
        self.nombre=nombre
        self.empleados=dict()
        self.clientes=dict()
        self.contrasena_ing_personal=contrasena_ing_personal
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
                    cliente=Cliente(nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado)
                    #mandar info al archivo 
                    self.clientes[usuario]=cliente
                
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
        

        
    #hacer una funcion para mostrar que el hotel esta guardando informacion
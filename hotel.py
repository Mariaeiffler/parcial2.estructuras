from Personal import Personal
from cliente import Cliente
from Persona import Persona
from validaciones import *
from Abrir_archivo import *
import pickle
class Hotel():
    def __init__(self):
        self.empleados=dict()
        self.clientes=dict()
    def entrar(self):
        pregunta=input('Elija una de las siguientes opciones: 1. Sign up \n 2.Sign in')
        validacionpregunta(pregunta)
        #validacion 
        match pregunta:
            case 1:
                #validar que no exista el usuario
                #validar todos los atributos
                nombre=input('Introduzca su nombre:')
                dni=input('Ingrese su DNI:')
                validaciondni(dni)
                direccion=input('Ingrese su direccion:')
                contacto=input('Ingrese su numero de contacto:')
                fecha_nac=input('Ingrese su fecha de nacimiento:')
                mail=input('Ingrese su mail:')
                usuario=input('Escriba el nombre de usuario:')
                contrasena=input('Escriba la contrasena:')
                validacioncontrasena(contrasena) #verificar el nombre de la funcion
                soy_empleado=input('Sos empleado? (responder si o no en minuscula)')
                validacionempleado(soy_empleado)
                
                if soy_empleado:
                    contrasena_personal=input('Ingrese la contrasena del personal:')
                    #validar contrasena personal (definida por nosotras)
                    personal=Personal.Personal(nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado)
                    #mandar info a archivo. 
                    self.empleados[usuario]=personal
                else:
                    cliente=cliente.Cliente(nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado)
                    #mandar info al archivo 
                    self.clientes[usuario]=cliente
                
            case 2:
                #validar que exista el usuario y que la contrasena sea correcta
                usuario=input('Escriba el nombre de usuario:')
                contrasena=input('Escriba la contrasena:')
    def save(self): #CHEQUEAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        with open('hotel.pickle','wb') as f:
            pickle.dump(self,f)

        
    #hacer una funcion para mostrar que el hotel esta guardando informacion
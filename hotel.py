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
        
    def obtener_habitaciones(self):
        try:
            with open('Habitaciones.csv', 'r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)                       
                for fila in lector:
                    for i in fila:
                        lista = []
                        lista.append(i)
                        self.habitaciones.append(lista)
        except FileNotFoundError:
            with open('Habitaciones.csv', 'w', encoding='utf-8') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerow(crear_habitaciones_simples())
                escritor_csv.writerow(crear_habitaciones_dobles())
                escritor_csv.writerow(crear_habitaciones_suite())
            #preguntar como hacemos para que se pase bien a la lista
        return (self.habitaciones)

        
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
        usuario = self.entrar()
        #no se si ponerlo asi esta bien
        habitaciones = Hotel.obtener_habitaciones(self)
        habitacion = validacion_preg_hab()
        fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
        fecha_inicio = convertirfecha_datetime(fecha_inicio)
        fecha_finalizacion = input('Ingrese la fecha de finaliación de su estadia en el formato dd/mm/aaaa')
        fecha_finalizacion = convertirfecha_datetime(fecha_finalizacion)
        #habría que fijarnos de ver si hay habitaciones d ese tipo libres en esas fechas
        self.clientes[usuario].reservas.append(fecha_inicio)
        self.clientes[usuario].reservas.append(fecha_finalizacion)
        # match pregunta:
        #     case 1:
        return
     
if __name__ == "__main__":
    hotel = Hotel('POO')
    entrar = Hotel.obtener_habitaciones(hotel)
    print(entrar)
    #hacer una funcion para mostrar que el hotel esta guardando informacion
 
 
   
## MENU BUFFET 
  
def mostrar_menu():
    print("Menú buffet:")
    print("1. Desayuno")
    print("2. Almuerzo")
    print("3. Cena")

def menu_desayuno():
    print("\nDesayuno:")
    opcion = input("Selecciona una opción de desayuno (1-6): ")
    match opcion:
        case "1":
            "Infusión (Café con leche/Té/Jugo de Naranja) - $500"
            pedido= pedido_buffet('Infusion')
        case "2":
            "Tostadas con queso y mermelada - $700"
            pedido= pedido_buffet('Tostadas')
        case "3":
            "Yogur con cereales - $600"
            pedido= pedido_buffet('Yogur')
        case '4':
            'Huevos revueltos - $800'
            pedido= pedido_buffet('Huevos')
        case '5':
            'Facturas - $600'
            pedido= pedido_buffet('Facturas')
        case '6':
            'Ensalada de frutas - $750'
            pedido= pedido_buffet('Ensalada')
        case _:
            "Opción no válida"

    print(opcion)

def menu_almuerzo():
    print("\nAlmuerzo:")
    opcion = input("Selecciona una opción de almuerzo (1-7): ")
    match opcion:
        case "1":
            "Pollo/Carne con guarnición - $2000"
            pedido= pedido_buffet('Pollo/Carne')
        case "2":
            "Sopa del día - $1500"
            pedido= pedido_buffet('Sopa')
        case "3":
            "Ensalada 4 toppings - $1000"
            pedido= pedido_buffet('Ensalada')
        case '4':
            'Pesca del día- $3000'
            pedido= pedido_buffet('Pesca')
        case '5':
            'Opción vegetariana (hamburguesa de lentejas con papas fritas)- $1500'
            pedido= pedido_buffet('Vegetariano')
        case '6':
            'Pastas (ravioles, ñoquis, sorrentinos)- $1500'
            pedido= pedido_buffet('Pastas')
        case '7':
            'Postres (flan con dulce de leche, bocha de helado, tiramisú)- $500 (c/u)'
            pedido= pedido_buffet('Postres')
        case _:
            "Opción no válida"

    print(opcion)

def menu_cena():
    print("\nCena:")
    opcion = input("Selecciona una opción de cena (1-7): ")
    match opcion:
        case "1":
            "Salmón a la parrilla con puré de papas - $4000"
            pedido= pedido_buffet('Salmón')
        case "2":
            "Pastas (ravioles, ñoquis, sorrentinos)- $1500"
            pedido= pedido_buffet('Pastas')
        case "3":
            'Opción vegetariana (falafel) - $1500'
            pedido= pedido_buffet('Vegetariana')
        case '4':
            'Pizza (muzzarella, napolitana, fugazzeta, calabresa) - $2000)'
            pedido= pedido_buffet('Pizza')
        case '5':
            'Empanadas (carne, pollo, jamón y queso, verdura) - $600 (c/u))'
            pedido= pedido_buffet('Empanadas')
        case '6':
            'Asado con papas fritas - $3000 (para 2 personas) (se puede pedir para 1 persona por $2000)'
            pedido= pedido_buffet('Asado')
        case '7':
            'Postres (flan con dulce de leche, bocha de helado, tiramisú)- $500 (c/u)'
            pedido= pedido_buffet('Postres')
        case _:
            "Opción no válida"

    print(opcion)

def main():
    while True:
        mostrar_menu()
        opcion_comida = input("Selecciona una comida del día (1 para desayuno/merienda, 2 para almuerzo, 3 para cena, listo para salir): ")

        match opcion_comida:
            case "1":
                menu_desayuno()
            case "2":
                menu_almuerzo()
            case "3":
                menu_cena()
            case "listo":
                break
            case _:
                print("Opción no válida. Por favor, selecciona una comida válida.")

def pedidos_buffet(pedido):
    cola= []
    cola.insert(0,pedido)
    return cola 
    
def realizar_pedido():
    self.cola.pop()

if __name__ == "__main__":
    main()
    
    



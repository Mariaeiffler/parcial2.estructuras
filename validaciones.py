from datetime import *  
from hotel import *  

def validacionpregunta(pregunta):
    validacion = False
    while validacion == False:
        try:
            int(pregunta)
            pregunta = int(pregunta)
            validacion = True
        except Exception:
            pregunta = input('Elija una de las siguientes opciones: 1. Sign up \n 2. Sign in  ')
    if pregunta != 1 and pregunta != 2:
        pregunta = input('Elija una de las siguientes opciones: 1. Sign up \n 2. Sign in  ')
        while pregunta != 1 and pregunta != 2:
            pregunta = input('Elija una de las siguientes opciones: 1. Sign up \n 2. Sign in  ')
    return pregunta


        
def validaciondni(dni):
    if str(dni).isdigit() == False or len(str(dni)) != 8:
        dni = input('Ingrese su DNI  ')
        while str(dni).isdigit() == False or len(str(dni)) != 8:
            dni = input('Ingrese su DNI  ')
    ## agregar tambien que no se repita
    return dni

def cantidad_mayusculas(contrasena):
    contador = 0
    for digito in contrasena:
        if digito.isupper() == True:
            contador += 1
    return contador

def cantidad_numero(contrasena):
    contador = 0
    for digito in contrasena:
        if digito.isdigit() == True:
            contador +=1
    return contador
            
def validacioncontrasena(contrasena):
    if cantidad_mayusculas(contrasena) < 1  or cantidad_numero(contrasena) <1:
        contrasena = input ('Ingrese una contraseña valida ')
        while cantidad_mayusculas(contrasena) < 1  or cantidad_numero(contrasena) <1:
            contrasena = input ('Ingrese una contraseña valida ')
    return contrasena

def validacionempleado(soy_empleado):
    if soy_empleado != 'si' and soy_empleado != 'no':
        soy_empleado = input('Ingrese si, si es empleado y no si no lo es (en minuscula) ')
        while soy_empleado != 'si' and soy_empleado != 'no':
            soy_empleado = input('Ingrese si, si es empleado y no si no lo es (en minuscula) ')
    if soy_empleado == 'si':
        return True
    else:
        return False
    
def validacionnombre1(nombre):
    validacion = True
    for digito in nombre:
        if digito.isalpha == False or digito.whitespace == False:
            validacion = False
    return validacion
    
def validacionnombre2(nombre):
    validacion = validacionnombre1(nombre)
    if validacion == False:
        nombre = input('Ingrese su nombre y apellido ')
        validacion = validacionnombre1(nombre)
        while validacion == False:
            nombre = input('Ingrese su nombre y apellido ')
            validacion = validacionnombre1(nombre)
    return nombre
            
def validacioncontacto(contacto):
    if cantidad_numero(contacto) != len(str(contacto)) or cantidad_numero(contacto) != 8:
        contacto = input('Ingrese su numero de telefono con el formato 911... ')
        while cantidad_numero(contacto) != len(str(contacto)) or cantidad_numero(contacto) != 8:
            contacto = input('Ingrese su numero de telefono con el formato 911... ')
    return contacto

def validacionusuario(usuario):
    if len(str(usuario)) < 5:
        usuario = input('Ingrese un nombre de usuario válido (con minimo 5 dígitos) ')
        while len(str(usuario)) < 5:
            usuario = input('Ingrese un nombre de usuario válido (con minimo 5 dígitos) ')  
    return usuario

def convertirfecha_datetime(fecha):
    validacion = False
    while validacion == False:
        try:
            fecha_datetime = datetime.strptime(fecha, '%d/%m/%Y')
            validacion = True
            return fecha_datetime
        except Exception:
            fecha = input('Ingrese la fecha en el formato dd/mm/yyyy ')
            
def mayoredad (fecha):
    if type(fecha) == datetime:
        fecha_datetime = fecha
    else:
        fecha_datetime = convertirfecha_datetime(fecha)
    diferencia:datetime = date.today() - fecha_datetime.date()
    dias = abs(diferencia.days)
    anio = dias / 365
    if anio >= 16:
        return True
    else:
        return False
    
def validacionfechanac (fecha):
    fecha_datetime = convertirfecha_datetime(fecha)
    if mayoredad(fecha_datetime) == False:
        fecha = input('Ingrese la fecha en el formato dd/mm/yyyy ')
        fecha_datetime = convertirfecha_datetime(fecha)
        while mayoredad(fecha_datetime) == False:
            fecha = input('Ingrese la fecha en el formato dd/mm/yyyy ')
            fecha_datetime = convertirfecha_datetime(fecha)
    return fecha_datetime

def validacion_h(pregunta1, valor1, valor2):
    validacion = True
    if pregunta1[0] != 'h':
        validacion = False
    numero = pregunta1[1]
    try:
        numero = int(numero)
    except Exception:
        validacion = False
    if numero not in range (valor1,valor2+1):
    #esta bien este range????????
        validacion = False
    return validacion

def validacionpregunta2(pregunta):
    validacion = False
    while validacion == False:
        try:
            int(pregunta)
            pregunta = int(pregunta)
            validacion = True
        except Exception:
            pregunta = input('Elija una de las siguientes habitaciones: \n 1. Simple ($5000 - $15000) \n 2. Doble ($20000 - $30000) \n 3. Suite ($35000 - $45000) ')
    pregunta = str(pregunta)
    if pregunta != '1' and pregunta != '2' and pregunta != '3':
         pregunta = input('Elija una de las siguientes habitaciones: \n 1. Simple ($5000 - $15000) \n 2. Doble ($20000 - $30000) \n 3. Suite ($35000 - $45000) ')
    while pregunta != '1' and pregunta != '2' and pregunta != '3':
        pregunta = input('Elija una de las siguientes habitaciones: \n 1. Simple ($5000 - $15000) \n 2. Doble ($20000 - $30000) \n 3. Suite ($35000 - $45000) ')
    return int(pregunta)
        
def validacion_preg_hab():
    pregunta = input('Elija una de las siguientes habitaciones: \n 1. Simple ($5000 - $15000) \n 2. Doble ($20000 - $30000) \n 3. Suite ($35000 - $45000) ')
    pregunta = validacionpregunta2(pregunta)
    match pregunta:
        case 1:
            pregunta1 = input('Elija una de las siguientes opciones: \n h1: Sin baño privado y sin balcón ($5000) \n h2: Con baño y sin balcón ($10000) \n h3: Con baño privado y sin balcón ($10000) \n h4: Con baño privado y con balcón ($15000) ')
            if len(pregunta1) != 2:
                pregunta1 = input('Elija una de las siguientes opciones: \n h1: Sin baño privado y sin balcón ($5000) \n h2: Con baño y sin balcón ($10000) \n h3: Con baño privado y sin balcón ($10000) \n h4: Con baño privado y con balcón ($15000) ')
                while len(pregunta1) != 2:
                    pregunta1 = input('Elija una de las siguientes opciones: \n h1: Sin baño privado y sin balcón ($5000) \n h2: Con baño y sin balcón ($10000) \n h3: Con baño privado y sin balcón ($10000) \n h4: Con baño privado y con balcón ($15000) ')
            validacion = validacion_h(pregunta1,1, 4)
            while(validacion == False):
                pregunta1 = input('Elija una de las siguientes opciones: \n h1: Sin baño privado y sin balcón ($5000) \n h2: Con baño y sin balcón ($10000) \n h3: Con baño privado y sin balcón ($10000) \n h4: Con baño privado y con balcón ($15000)')
                validacion = validacion_h(pregunta1,1,4)
            return pregunta1
        case 2:
            pregunta1 = input('Elija una de las siguientes opciones: \n h5: Sin baño privado y sin balcón ($20000) \n h6: Con baño y sin balcón ($25000) \n h7: Con baño privado y sin balcón ($25000) \n h8: Con baño privado y con balcón ($30000) ')
            if len(pregunta1) != 2:
                pregunta1 = input('Elija una de las siguientes opciones: \n h5: Sin baño privado y sin balcón ($20000) \n h6: Con baño y sin balcón ($25000) \n h7: Con baño privado y sin balcón ($25000) \n h8: Con baño privado y con balcón ($30000) ')
                while len(pregunta1) != 2:
                    pregunta1 = input('Elija una de las siguientes opciones: \n h5: Sin baño privado y sin balcón ($20000) \n h6: Con baño y sin balcón ($25000) \n h7: Con baño privado y sin balcón ($25000) \n h8: Con baño privado y con balcón ($30000) ')
            validacion = validacion_h(pregunta1,5,8)
            while(validacion == False):
                pregunta1 = input('Elija una de las siguientes opciones: \n h5: Sin baño privado y sin balcón ($20000) \n h6: Con baño y sin balcón ($25000) \n h7: Con baño privado y sin balcón ($25000) \n h8: Con baño privado y con balcón ($30000) ')
                validacion = validacion_h(pregunta1,5,8)
            return pregunta1
        case 3:
            pregunta1 = input('Elija una de las siguientes opciones: \n h9: Sin baño privado y sin balcón ($35000) \n h10: Con baño y sin balcón ($40000) \n h11: Con baño privado y sin balcón ($40000) \n h12: Con baño privado y con balcón ($45000) ')
            if len(pregunta1) != 2:
                pregunta1 = input('Elija una de las siguientes opciones: \n h9: Sin baño privado y sin balcón ($35000) \n h10: Con baño y sin balcón ($40000) \n h11: Con baño privado y sin balcón ($40000) \n h12: Con baño privado y con balcón ($45000) ')
                while len(pregunta1) != 2:
                    pregunta1 = input('Elija una de las siguientes opciones: \n h9: Sin baño privado y sin balcón ($35000) \n h10: Con baño y sin balcón ($40000) \n h11: Con baño privado y sin balcón ($40000) \n h12: Con baño privado y con balcón ($45000) ')
            validacion = validacion_h(pregunta1,9,12)
            while(validacion == False):
                pregunta1 = input('Elija una de las siguientes opciones: \n h9: Sin baño privado y sin balcón ($35000) \n h10: Con baño y sin balcón ($40000) \n h11: Con baño privado y sin balcón ($40000) \n h12: Con baño privado y con balcón ($45000) ')
                validacion = validacion_h(pregunta1,9,12)
            return pregunta1
            
            
        
if __name__=="__main__":
    validacion = validacion_preg_hab()



    
def mostrar_menu():
    print("Menú buffet:")
    print("1. Desayuno")
    print("2. Almuerzo")
    print("3. Cena")

# def menu_desayuno():
#     print("\nDesayuno:")
#     opcion = input("Selecciona una opción de desayuno (1-6): ")
#     plato = match opcion:
#         case "1":
#             "Infusión (Café con leche/Té/Jugo de Naranja) - $500"
#         case "2":
#             "Tostadas con queso y mermelada - $700"
#         case "3":
#             "Yogur con cereales - $600"
#         case '4':
#             'Huevos revueltos - $800'
#         case '5':
#             'Facturas - $600'
#         case '6':
#             'Ensalada de frutas - $750'
#         case _:
#             "Opción no válida"

#     print(plato)

# def menu_almuerzo():
#     print("\nAlmuerzo:")
#     opcion = input("Selecciona una opción de almuerzo (1-7): ")
#     plato = match opcion:
#         case "1":
#             "Pollo/Carne con guarnición - $2000"
#         case "2":
#             "Sopa del día - $1500"
#         case "3":
#             "Ensalada 4 toppings - $1000"
#         case '4':
#             'Pesca del día- $3000'
#         case '5':
#             'Opción vegetariana (hamburguesa de lentejas con papas fritas)- $1500'
#         case '6':
#             'Pastas (ravioles, ñoquis, sorrentinos)- $1500'
#         case '7':
#             'Postres (flan con dulce de leche, bocha de helado, tiramisú)- $500 (c/u)'
#         case _:
#             "Opción no válida"

#     print(plato)

# def menu_cena():
#     print("\nCena:")
#     opcion = input("Selecciona una opción de cena (1-7): ")
#     plato = match opcion:
#         case "1":
#             "Salmón a la parrilla con puré de papas - $4000"
#         case "2":
#             "Pastas (ravioles, ñoquis, sorrentinos)- $1500"
#         case "3":
#             'Opción vegetariana (falafel) - $1500'
#         case '4':
#             'Pizza (muzzarella, napolitana, fugazzeta, calabresa) - $2000)'
#         case '5':
#             'Empanadas (carne, pollo, jamón y queso, verdura) - $600 (c/u))'
#         case '6':
#             'Asado con papas fritas - $3000 (para 2 personas) (se puede pedir para 1 persona por $2000)'
#         case '7':
#             'Postres (flan con dulce de leche, bocha de helado, tiramisú)- $500 (c/u)'
#         case _:
#             "Opción no válida"

#     print(plato)

# def main():
#     while True:
#         mostrar_menu()
#         opcion_comida = input("Selecciona una comida del día (1 para desayuno/merienda, 2 para almuerzo, 3 para cena, listo para salir): ")

#         plato = match opcion_comida:
#             case "1":
#                 menu_desayuno()
#             case "2":
#                 menu_almuerzo()
#             case "3":
#                 menu_cena()
#             case "listo":
#                 break
#             case _:
#                 print("Opción no válida. Por favor, selecciona una comida válida.")

# if __name__ == "__main__":
#     main()
    
    



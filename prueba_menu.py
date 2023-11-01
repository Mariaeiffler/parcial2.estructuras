from datetime import *
from cliente import Cliente

def val_int(x): #valida que sea un entero
        try:
            num=int(x)
            return True
        except Exception:
            return False
        
def val_opc(opcion): #valida las opciones del menu ppl
    validacion=False
    while validacion == False:
        if val_int(opcion):
            x=int(opcion)
            if x==1 or x==2:
                validacion=True
            else:
                opcion = input('Error. Elija una de las siguientes opciones: \n 1. Sign up \n 2. Sign in \n')
        else: 
            opcion = input('Error. Elija una de las siguientes opciones: \n 1. Sign up \n 2. Sign in \n')
    return x

def valNombre1(nombre):
    validacion = True
    for digito in nombre:
        if digito.isalpha() == False and digito.isspace() == False:
            validacion = False
    return validacion
    

def valNombre2 (nombre):
    validacion = valNombre1(nombre)
    while validacion == False:
        nombre = input('Ingrese su nombre y apellido: ')
        validacion = valNombre1(nombre)
    return nombre

def validaciondni(dni): #TODO: agregar tambien que no se repita --> esta no la toque
    if str(dni).isdigit() == False or len(str(dni)) != 8:
        dni = input('Ingrese su DNI  ')
        while str(dni).isdigit() == False or len(str(dni)) != 8:
            dni = input('Ingrese su DNI  ')
    return dni

def cantidad_numero(contrasena): # --> esta no la toque
    contador = 0
    for digito in contrasena:
        if digito.isdigit() == True:
            contador +=1
    return contador

def validacioncontacto(contacto):
    while cantidad_numero(contacto) != len(str(contacto)) or cantidad_numero(contacto) != 13:
        contacto = input('Ingrese su numero de telefono con el formato 54911... ')
    return contacto

def convertirfecha_datetime(fecha): # --> no la toque 
    validacion = False
    while validacion == False:
        try:
            fecha_datetime = datetime.strptime(fecha, '%d/%m/%Y')
            validacion = True
            return fecha_datetime
        except Exception:
            fecha = input('Ingrese la fecha en el formato dd/mm/yyyy ')
            
def mayoredad (fecha): # --> no la toque
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

def validacionfechanac (fecha): # --> no la toque 
    fecha_datetime = convertirfecha_datetime(fecha)
    if mayoredad(fecha_datetime) == False:
        fecha = input('Ingrese la fecha en el formato dd/mm/yyyy: ')
        fecha_datetime = convertirfecha_datetime(fecha)
        while mayoredad(fecha_datetime) == False:
            fecha = input('Ingrese la fecha en el formato dd/mm/yyyy: ')
            fecha_datetime = convertirfecha_datetime(fecha)
    return fecha_datetime

def valMail (mail): #validar algo más?
    while mail.count('@')!=1:
        mail=input('Ingrese su mail:')
        
def validacionusuario(usuario): #TODO:chequear que no este repetido
    while len(str(usuario)) < 5:
        usuario = input('Ingrese un nombre de usuario válido (con minimo 5 dígitos) ')  
    return usuario

def cantidad_mayusculas(contrasena): # --> no la toque
    contador = 0
    for digito in contrasena:
        if digito.isupper() == True:
            contador += 1
    return contador

def validacioncontrasena(contrasena): 
    while cantidad_mayusculas(contrasena) < 1  or cantidad_numero(contrasena) <1:
        contrasena = input ('Ingrese una contraseña valida, que contenga una mayuscula y un numero: ')
    return contrasena

def infoPersonas ():
    nombre=input('Introduzca su nombre y apellido: ')
    nombre=valNombre2(nombre)
    dni=input('Ingrese su DNI: ')
    dni=validaciondni(dni)
    direccion=input('Ingrese su direccion: ') #es necesario validar la dirección?
    contacto=input('Ingrese su numero de contacto: ')
    contacto=validacioncontacto(contacto)
    fecha_nac=input('Ingrese su fecha de nacimiento: ')
    fecha_nac=validacionfechanac (fecha_nac)
    mail=input('Ingrese su mail: ')
    mail=valMail(mail)
    usuario=input('Escriba el nombre de usuario: ')
    usuario=validacionusuario(usuario)
    contrasena=input('Escriba una contrasena que contenga por lo menos una mayuscula y un numero: ')
    contrasena=validacioncontrasena(contrasena)
    return nombre,dni,direccion,contacto,fecha_nac,mail,usuario,contrasena

def valiExiUsu (diccionario:dict, usuario:str):
    if usuario not in diccionario:
        return False
    else: 
        return True

# def valiSignIn (usuario,contrasena,dic1:dict,dic2:dict):
#     while usuario not in (dic1 or dic2) or : --> chequear que pertenezca al diccionario de empleadps o de clientes y verificar que la contraseña sea la que corresponde al usuario 
        
    
clientesDict=dict()  # --> cree este diccionario de clientes para mostrar como habría que agregarlo mas o menos 
empleadosDict=dict() # --> mismo que arriba

def menuPPL(): 
    opcion =input(('Elija una de las siguientes opciones: \n 1. Sign up \n 2.Sign in \n'))
    opcion=val_opc (opcion)
    match opcion:
        case 1:
            nombre,dni,direccion,contacto,fecha_nac,mail,usuario,contrasena=infoPersonas()
            empleado=False
            cliente=Cliente(nombre,usuario,dni,direccion,contacto,fecha_nac,mail,empleado,contrasena) #creo que el soyEmpleado en cliente esta de mas
            clientesDict[cliente.dni]= cliente # --> chequear que funcione bien lo de agregarse al diccionario y fijarse si queremos que la llave sea el dni o el nombre de usuario, tal vez no hace falta el cliente antes del dni pero si hay que agregar el self adelante del diccionario 
        case 2:
            usuario=input('Escriba el nombre de usuario: ')
            contrasena=input('Escriba una contrasena que contenga por lo menos una mayuscula y un numero: ')
            # usuario,contrasena=valiSignIn(usuario,contrasena,clientesDict,empleadosDict)
            
            
if __name__=='__main__':
   dni='mili'
   dni=validacioncontrasena(dni)
   print (dni)
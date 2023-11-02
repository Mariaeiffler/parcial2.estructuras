from datetime import *
from cliente import Cliente
from Habitacion_Doble import *
from Habitacion_Simple import *
from Habitacion_Suite import *

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
            fecha = input('Ingrese la fecha en el formato dd/mm/aaaa ')
            
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
    return mail
        
def validacionusuario(usuario): #TODO:chequear que no este repetido
    while len(str(usuario)) < 5:
        usuario = input('Ingrese un nombre de usuario válido (con minimo 5 dígitos) ')  
    #habría q ver tambien que no tenga espacios
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
    # en esta validacion no se fija q no tenga espacios? si tiene q poner su nombre y apellido tiene q tener un espacio
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
    return nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena

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
            
            
#if __name__=='__main__':
#    dni='mili'
#    dni=validacioncontrasena(dni)
#    print (dni)           
            
            
##################################################################################################################################################
def valiPregCliente(pregcliente):
    validacion=False
    while validacion == False:
        if val_int(opcion):
            x=int(opcion)
            if x==1 or x==2 or x==3 or x==4:
                validacion=True
            else:
                opcion = input('Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n')
        else: 
            opcion = input('Error. Elija una de las siguientes opciones: \n 1. Hacer una reserva \n 2. Hacer un pedido en el buffet \n 3. Modificar una reserva \n 4. Cancelar una reserva \n')
    return x

def crearHab():
    h1 = Habitacion_Simple(1,1,1,[],5000,10000,2,False,False)
    h2 = Habitacion_Simple(2,1,1,[],10000,10000,2,True,False)
    h3 = Habitacion_Simple(3,1,1,[],10000,10000,2,False,True)
    h4 = Habitacion_Simple(4,1,1,[],15000,10000,2,True,True)
    h5 = Habitacion_Doble(5,2,1,[],20000,10000,4,False,False)
    h6 = Habitacion_Doble(6,2,1,[],25000,10000,4,True,False)
    h7 = Habitacion_Doble(7,2,1,[],25000,10000,4,False,True)
    h8 = Habitacion_Doble(8,2,1,[],30000,10000,4,True,True)
    h9 = Habitacion_Suite(9,2,1,[],35000,10000,4,False,False)
    h10 = Habitacion_Suite(10,2,1,[],40000,10000,4,True,False)
    h11 = Habitacion_Suite(11,2,1,[],40000,10000,4,False,True)
    h12 = Habitacion_Suite(12,2,1,[],45000,10000,4,True,True)
    return (h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12)

def validacion_h(pregunta1, valor1, valor2):
    validacion = val_int(pregunta1)
    if validacion == True:
        if int(pregunta1) > valor1 and int(pregunta1) < valor2:
            habitacion = int(pregunta1)
        else:
            validacion = False
    return validacion

def validacionpregunta2(pregunta):
    validacion = False
    while validacion == False:
<<<<<<< HEAD
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
        
=======
        if val_int(pregunta):
            x=int(pregunta)
            if x==1 or x==2 or x==3:
                validacion=True
            else:
                pregunta = input('Error. Elija una de las siguientes habitaciones: \n 1. Simple ($5000 - $15000) \n 2. Doble ($20000 - $30000) \n 3. Suite ($35000 - $45000) \n')
        else: 
            pregunta = input('Error. Elija una de las siguientes habitaciones: \n 1. Simple ($5000 - $15000) \n 2. Doble ($20000 - $30000) \n 3. Suite ($35000 - $45000) \n')
    return x
    
>>>>>>> 6a7675cc4f705650a9559f3cd374e8c33456c0e2
def validacion_preg_hab():
    pregunta = input('Elija una de las siguientes habitaciones: \n 1. Simple ($5000 - $15000) \n 2. Doble ($20000 - $30000) \n 3. Suite ($35000 - $45000) \n')
    pregunta = validacionpregunta2(pregunta)
    match pregunta:
        case 1:
<<<<<<< HEAD
            pregunta1 = input('Elija una de las siguientes opciones: \n 1: Sin baño privado y sin balcón ($5000) \n 2: Con baño y sin balcón ($10000) \n 3: Con baño privado y sin balcón ($10000) \n 4: Con baño privado y con balcón ($15000) ')
            if len(pregunta1) != 2:
                pregunta1 = input('Elija una de las siguientes opciones: \n 1: Sin baño privado y sin balcón ($5000) \n 2: Con baño y sin balcón ($10000) \n 3: Con baño privado y sin balcón ($10000) \n 4: Con baño privado y con balcón ($15000) ')
                while len(pregunta1) != 2:
                    pregunta1 = input('Elija una de las siguientes opciones: \n 1: Sin baño privado y sin balcón ($5000) \n 2: Con baño y sin balcón ($10000) \n 3: Con baño privado y sin balcón ($10000) \n 4: Con baño privado y con balcón ($15000) ')
=======
            pregunta1 = input('Elija una de las siguientes opciones: \n 1: Sin baño privado y sin balcón ($5000) \n 2: Con baño y sin balcón ($10000) \n 3: Con baño privado y sin balcón ($10000) \n 4: Con baño privado y con balcón ($15000) \n')
>>>>>>> 6a7675cc4f705650a9559f3cd374e8c33456c0e2
            validacion = validacion_h(pregunta1,1, 4)
            while(validacion == False):
                pregunta1 = input('Elija una de las siguientes opciones: \n 1: Sin baño privado y sin balcón ($5000) \n 2: Con baño y sin balcón ($10000) \n 3: Con baño privado y sin balcón ($10000) \n 4: Con baño privado y con balcón ($15000)  \n')
                validacion = validacion_h(pregunta1,1,4)
            return pregunta1
        case 2:
            pregunta1 = input('Elija una de las siguientes opciones: \n 5: Sin baño privado y sin balcón ($20000) \n 6: Con baño y sin balcón ($25000) \n 7: Con baño privado y sin balcón ($25000) \n 8: Con baño privado y con balcón ($30000) \n')
            validacion = validacion_h(pregunta1,5,8)
            while(validacion == False):
                pregunta1 = input('Elija una de las siguientes opciones: \n 5: Sin baño privado y sin balcón ($20000) \n 6: Con baño y sin balcón ($25000) \n 7: Con baño privado y sin balcón ($25000) \n 8: Con baño privado y con balcón ($30000) \n')
                validacion = validacion_h(pregunta1,5,8)
            return pregunta1
        case 3:
            pregunta1 = input('Elija una de las siguientes opciones: \n 9: Sin baño privado y sin balcón ($35000) \n 10: Con baño y sin balcón ($40000) \n 11: Con baño privado y sin balcón ($40000) \n 12: Con baño privado y con balcón ($45000) \n')
            validacion = validacion_h(pregunta1,9,12)
            while(validacion == False):
                pregunta1 = input('Elija una de las siguientes opciones: \n 9: Sin baño privado y sin balcón ($35000) \n 10: Con baño y sin balcón ($40000) \n 11: Con baño privado y sin balcón ($40000) \n 12: Con baño privado y con balcón ($45000) \n')
                validacion = validacion_h(pregunta1,9,12)
            return pregunta1
        
<<<<<<< HEAD
def comparacion_fechas(fecha_inicio, fecha_finalizacion):
    if fecha_inicio < datetime.now():
        print('Su fecha de inicio de la estadía no es valida ')
        fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
        fecha_inicio = convertirfecha_datetime(fecha_inicio)
        while fecha_inicio < datetime.now():
            fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
            fecha_inicio = convertirfecha_datetime(fecha_inicio)
        fecha_finalizacion = input('Ingrese la fecha de finaliación de su estadia en el formato dd/mm/aaaa ')
        fecha_finalizacion = convertirfecha_datetime(fecha_finalizacion)
    if fecha_inicio > fecha_finalizacion:
        print('Su fecha de finalización es antes que su fecha de inicio de la estadía')
        fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
        fecha_inicio = convertirfecha_datetime(fecha_inicio)
        fecha_finalizacion = input('Ingrese la fecha de finaliación de su estadia en el formato dd/mm/aaaa ')
        fecha_finalizacion = convertirfecha_datetime(fecha_finalizacion)
        while fecha_inicio > fecha_finalizacion:
=======
def comp_fecha_hoy(fecha_inicio):
    validacion = False
    while validacion == False:
        if (fecha_inicio > datetime.today())==False:
            print('Su fecha de inicio de la estadía no es valida ')
            fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
            fecha_inicio = convertirfecha_datetime(fecha_inicio)
        else:
            validacion = True
    return fecha_inicio
        
def comparacion_fechas(fecha_inicio):
    fecha_inicio = comp_fecha_hoy(fecha_inicio)
    fecha_finalizacion = input('Ingrese la fecha de finaliación de su estadia en el formato dd/mm/aaaa ')
    fecha_finalizacion = convertirfecha_datetime(fecha_finalizacion)
    validacion = False
    while validacion == False:
        if (fecha_inicio < fecha_finalizacion)==False:
>>>>>>> 6a7675cc4f705650a9559f3cd374e8c33456c0e2
            print('Su fecha de finalización es antes que su fecha de inicio de la estadía')
            fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
            fecha_inicio = convertirfecha_datetime(fecha_inicio)
            fecha_inicio = comp_fecha_hoy(fecha_inicio)
            fecha_finalizacion = input('Ingrese la fecha de finaliación de su estadia en el formato dd/mm/aaaa ')
            fecha_finalizacion = convertirfecha_datetime(fecha_finalizacion)
<<<<<<< HEAD
    return fecha_inicio, fecha_finalizacion
=======
        else:
            validacion = True
    return fecha_inicio, fecha_finalizacion

def reserva():
    habitacion=validacion_preg_hab()
    # print('La habitación que usted ha seleccionado es {}'.format())#hacer q se printee el str d la habitacion
    fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
    fecha_inicio = convertirfecha_datetime(fecha_inicio)
    fecha_inicio, fecha_fin = comparacion_fechas(fecha_inicio)
    return fecha_inicio, fecha_fin, habitacion

def val_res(opcion):
    validacion=False
    while validacion == False:
        if val_int(opcion):
            x=int(opcion)
            if x==1 or x==2:
                validacion=True
            else:
                opcion = input('Error. Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n')
        else: 
            opcion = input('Error. Elija una opción: \n 1. Elegir otras fechas \n 2. Elegir otra habitación \n')
    return x
>>>>>>> 6a7675cc4f705650a9559f3cd374e8c33456c0e2

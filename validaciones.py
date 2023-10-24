from datetime import *

def validacionpregunta(pregunta):
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
    

        
        
if __name__=="__main__":
    fecha = '12/11/2009'
    validacion = validacionfechanac (fecha)
    print(validacion)







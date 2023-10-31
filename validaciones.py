from datetime import *  
from hotel import *  
from Reserva import Reserva
from cliente import Cliente

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
    if numero > valor1 and numero < valor2:
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
            
# if __name__=="__main__":
#      validacion = validacion_preg_hab()
#      print(validacion)
    
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
            print('Su fecha de finalización es antes que su fecha de inicio de la estadía')
            fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
            fecha_inicio = convertirfecha_datetime(fecha_inicio)
            fecha_finalizacion = input('Ingrese la fecha de finaliación de su estadia en el formato dd/mm/aaaa ')
            fecha_finalizacion = convertirfecha_datetime(fecha_finalizacion)
    return fecha_inicio, fecha_finalizacion

    
    



def realizar_reserva(usuario):
        habitacion = validacion_preg_hab()
        fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
        fecha_inicio = convertirfecha_datetime(fecha_inicio)
        fecha_finalizacion = input('Ingrese la fecha de finaliación de su estadia en el formato dd/mm/aaaa ')
        fecha_finalizacion = convertirfecha_datetime(fecha_finalizacion)
        fecha_inicio, fecha_finalizacion = comparacion_fechas(fecha_inicio, fecha_finalizacion)
        reserva = Reserva(usuario, fecha_inicio, fecha_finalizacion)
        return reserva
        
    # self.clientes[usuario].reservas.append(fecha_inicio)
        # self.clientes[usuario].reservas.append(fecha_finalizacion)
        # match pregunta:
        #     case 1:
    


if __name__ == "__main__":
    main()
    
    
if __name__=="__main__":
    fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
    fecha_inicio = convertirfecha_datetime(fecha_inicio)
    fecha_finalizacion = input('Ingrese la fecha de finaliación de su estadia en el formato dd/mm/aaaa ')
    fecha_finalizacion = convertirfecha_datetime(fecha_finalizacion)
    comp = comparacion_fechas(fecha_inicio, fecha_finalizacion)
    print(comp)


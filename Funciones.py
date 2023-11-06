from datetime import *
from Habitacion_Doble import *
from Habitacion_Simple import *
from Habitacion_Suite import *
import numpy as np
from Tareas_Empleados import *
from nodo import NodoTarea
import pickle

def obtener_pickle(hotel, accion):
    if accion == 'abrir':
        try:
            with open ('hotel.pickle','rb') as hpickle:
                info = pickle.load(hpickle)
            hotel.empleados = info.empleados
            hotel.clientes = info.clientes
            hotel.habitaciones = info.habitaciones
            hotel.reservas = info.reservas
            hotel.cobros = info.cobros
            hotel.buffet=info.buffet 
            hotel.tareas=info.tareas
            hotel.reservas=info.reservas
            hotel.bajasEmpleados=info.bajasEmpleados
        except FileNotFoundError:
            with open ('hotel.pickle','wb') as hpickle:
                pickle.dump(hotel,hpickle)
    else:
        with open ('hotel.pickle','wb') as hpickle:
            pickle.dump(hotel,hpickle)
        return

def cantidad_numero(contrasena):
    contador = 0
    for digito in contrasena:
        if digito.isdigit() == True:
            contador +=1
    return contador

def convertirfecha_datetime(fecha):
    validacion = False
    while validacion == False:
        try:
            fecha_datetime = datetime.strptime(fecha, '%d/%m/%Y')
            validacion = True
            return fecha_datetime
        except Exception:
            fecha = input('Ingrese la fecha en el formato dd/mm/aaaa: ')
            
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

def cantidad_mayusculas(contrasena):
    contador = 0
    for digito in contrasena:
        if digito.isupper() == True:
            contador += 1
    return contador

def valPalabraDic (palabra,dicc:dict):
    if palabra in dicc:
        return True
    else:
        return False
    
# if __name__=='__main__':
#     llaves=list(tareas_empleados.keys())
#     tipo=input('{} \n Ingrese el tipo de personal al que le quiere asignar una tarea: '.format(llaves))
#     tipo=valTipoEmpleado(tipo,tareas_empleados)
#     for i, tareas in enumerate (tareas_empleados[tipo]['tareas']):
#         print (F"{i} - {tareas}")
#     imprimir1='Ingrese la tarea que desea asignar: '
#     opcion=input(imprimir1)
#     tarea=valOpcAsignacion(opcion,tareas_empleados,tipo,'tareas',imprimir1)
#     print(tarea)    

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
            print('Su fecha de finalización es antes que su fecha de inicio de la estadía')
            fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
            fecha_inicio = convertirfecha_datetime(fecha_inicio)
            fecha_inicio = comp_fecha_hoy(fecha_inicio)
            fecha_finalizacion = input('Ingrese la fecha de finaliación de su estadia en el formato dd/mm/aaaa ')
            fecha_finalizacion = convertirfecha_datetime(fecha_finalizacion)
        else:
            validacion = True
    return fecha_inicio, fecha_finalizacion

def reserva():
    habitacion=validacion_preg_hab()
    fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
    fecha_inicio = convertirfecha_datetime(fecha_inicio)
    fecha_inicio, fecha_fin = comparacion_fechas(fecha_inicio)
    return fecha_inicio, fecha_fin, habitacion

def hab_ocupada(fecha_inicio, fecha_fin, hab, lista):
    val = False
    for habitacion in lista:
        if habitacion.numero == int(hab):
            if len(habitacion.reservas) == 0:
                val = True
            else:
                i = 0
                for estadia in habitacion.reservas:
                    if (estadia[0]>=fecha_fin) or (estadia[1]<=fecha_inicio):
                        i+=1
                if i == len(habitacion.reservas):
                    val = True
    if val == False:
        print('En las fechas ingresadas la habitación seleccionada ya está ocupada. Acá puede ver la ocupación de la misma:')
        for habitacion in lista:
            if habitacion.numero == int(hab):
                for res in habitacion.reservas:
                    print(res[0].strftime('%d/%m/%Y'), '-', res[1].strftime('%d/%m/%Y')) 
    return val

def modi_hab(val, preg, fecha_inicio, fecha_fin, hab, lista):
    while val == False:
        if preg == 1:
            fecha_inicio = input('Ingrese la fecha de inicio de su estadía en el formato dd/mm/aaaa ')
            fecha_inicio = convertirfecha_datetime(fecha_inicio)
            fecha_inicio, fecha_fin = comparacion_fechas(fecha_inicio)
            val = hab_ocupada(fecha_inicio, fecha_fin, hab, lista)
        if preg == 2:
            hab = validacion_preg_hab()
            val = hab_ocupada(fecha_inicio, fecha_fin, hab, lista)
        if preg == 3:
            fecha_inicio, fecha_fin, hab = reserva()
            val = hab_ocupada(fecha_inicio, fecha_fin, hab, lista)
    return val, fecha_inicio, fecha_fin, hab

def obtener_precio(lista, habitacion):
    for hab in lista:
        if int(hab.numero) == int(habitacion):
            monto=hab.precio
            objeto = hab
    return monto, objeto

def agregar_cobro(vector, cobro):
    vector = np.append(vector,[cobro])
    return vector

def crear_buffet(tupla):
    des = []
    almu = []
    cena = []
    otro = []
    for comida in tupla:
        if comida.tipo == 'desayuno':
            des.append(comida)
        elif comida.tipo == 'almuerzo':
            almu.append(comida)
        elif comida.tipo == 'cena':
            cena.append(comida)
        else:
            otro.append(comida)
    dic = {'desayuno':des, 'almuerzo':almu, 'cena':cena, 'otro':otro}
    return dic
    
def hacer_pedido(dic:dict):
    print('Ingrese una opción ')
    for i, comida in enumerate (dic):
        print (F"{i+1}. {comida}")
    preg = input('¿Que desea pedir del buffet? ')
    imprimir = 'Error. ¿Que desea pedir del buffet? '
    preg = val_opc(preg, 1, 4, imprimir)
    preg2=('Elija la comida que desea pedir ingresando el código ')
    imp = 'Elija la comida que desea pedir ingresando el código '
    if preg == 1:
        for comida in dic['desayuno']:
            print('{}.  {}'.format(comida.numero, comida))
        preg2 = val_opc(preg2, 1, 6, imp)
        monto, comida = obtener_precio(dic['desayuno'], preg2)
    elif preg == 2:
        for comida in dic['almuerzo']:
            print('{}.  {}'.format(comida.numero, comida))
        preg2 = val_opc(preg2, 7, 14, imp)
        monto, comida = obtener_precio(dic['almuerzo'], preg2)
    elif preg == 3:
        for comida in dic['cena']:
            print('{}.  {}'.format(comida.numero, comida))
        preg2 = val_opc(preg2, 15, 21, imp)
        monto, comida = obtener_precio(dic['cena'], preg2)
    else:
        for comida in dic['otro']:
            print('{}.  {}'.format(comida.numero, comida))
        preg2 = val_opc(preg2, 22, 22, imp)
        monto, comida = obtener_precio(dic['otro'], preg2)
    return monto, comida

def asignarTarea(tareas:dict,empleados:dict):
    llaves=list(tareas.keys())
    tipo=input('{} \n Ingrese el tipo de personal al que le quiere asignar una tarea: '.format(llaves))
    tipo=valTipoEmpleado(tipo,tareas)
    for i, tarea in enumerate (tareas[tipo]['tareas']):
        print (F"{i} - {tarea}")
    imprimir1='Ingrese la tarea que desea asignar: '
    opcionAsignar=input(imprimir1) 
    opcionAsignar=valOpcAsignacion(opcionAsignar,tareas,tipo,'tareas',imprimir1)
    for i, personal in enumerate (tareas[tipo]['empleados']):
        print (F"{i} - {personal}")
    imprimir2= 'Ingrese el número del usuario del empleados al que le desea asignar la tarea: '
    empleadoAsignar=input(imprimir2)
    empleadoAsignar=valOpcAsignacion(empleadoAsignar,tareas,tipo,'empleados',imprimir2)
    imprimir3='Error. Ingrese como nivel de importancia 1, 2 o 3 (siendo 1 el más urgente): '
    pregImportancia=input('Niveles de importancia: 1,2,3 (siendo 1 el más urgente). \n Ingrese la importancia de la tarea a realizar: ')
    importancia=val_opc(pregImportancia,1,3,imprimir3)
    nodoNuevo=NodoTarea(opcionAsignar,importancia)
    persona=empleados.get(empleadoAsignar) #chequear que me dice que es un string
    persona.tareasPendientes.agregarNodoTarea(nodoNuevo)
    return

def val_int(x): #valida que sea un entero
        try:
            num=int(x)
            return True
        except Exception:
            return False
        
def val_opc(opcion, valor1, valor2, imprimir): #valida las opciones del menu ppl
    validacion=False
    while validacion == False:
        if val_int(opcion):
            x=int(opcion)
            if x in range(valor1, valor2+1):
                validacion=True
            else:
                opcion = input(imprimir)
        else: 
            opcion = input(imprimir)
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

def validaciondni(dni,dic1:dict,dic2:dict): 
    vali1 = False
    vali2 = False
    while vali1 == False or vali2 == False:
        while str(dni).isdigit() == False or len(str(dni)) != 8:
            dni = input('Ingrese su DNI  ')
        if len(dic1) != 0:
            for cliente in dic1:
                if dic1.get(cliente).dni == dni:
                    dni = input('El DNI ingresado ya pertenece a otro usuario. Ingrese nuevamente su DNI  ')
                else:
                    vali1 = True
        else:
            vali1 = True
        if len(dic2) != 0:
            for emp in dic2:
                if dic2.get(emp).dni == dni:
                    dni = input('El DNI ingresado ya pertenece a otro usuario. Ingrese nuevamente su DNI  ')
                else:
                    vali2 = True
        else:
            vali2 = True
    return dni

def validacioncontacto(contacto):
    while cantidad_numero(contacto) != len(str(contacto)) or cantidad_numero(contacto) != 13:
        contacto = input('Ingrese su numero de telefono con el formato 54911... ')
    return contacto

def validacionfechanac (fecha): # --> no la toque 
    fecha_datetime = convertirfecha_datetime(fecha)
    if mayoredad(fecha_datetime) == False:
        fecha = input('Ingrese la fecha en el formato dd/mm/yyyy: ')
        fecha_datetime = convertirfecha_datetime(fecha)
        while mayoredad(fecha_datetime) == False:
            fecha = input('Ingrese la fecha en el formato dd/mm/yyyy: ')
            fecha_datetime = convertirfecha_datetime(fecha)
    return fecha_datetime

def valMail (mail):
    while mail.count('@')!=1 or mail.count('.')<1:
        mail=input('Error. Ingrese su mail (tiene que contener por lo menos un . y un @):')
    return mail

def validacionusuario(usuario,dic1,dic2): #TODO:chequear que no este repetido
    while len(str(usuario)) < 5 or valPalabraDic(usuario,dic1) or valPalabraDic(usuario,dic2):
        usuario = input('Su nombre de usuario no es válido, ingrese otro (con minimo 5 dígitos): ')  
    return usuario

def validacioncontrasena(contrasena): 
    while cantidad_mayusculas(contrasena) < 1  or cantidad_numero(contrasena) <1:
        contrasena = input ('Ingrese una contraseña valida, que contenga una mayuscula y un numero: ')
    return contrasena

def infoPersonas (dicc1:dict,dicc2:dict):   
    nombre=input('Introduzca su nombre y apellido: ')
    nombre=valNombre2(nombre)
    dni=input('Ingrese su DNI: ')
    dni=validaciondni(dni, dicc1, dicc2)
    direccion=input('Ingrese su direccion: ')
    contacto=input('Ingrese su numero de contacto: ')
    contacto=validacioncontacto(contacto)
    fecha_nac=input('Ingrese su fecha de nacimiento: (Debe ser mayor de edad para crearse un usuario) ')
    fecha_nac=validacionfechanac (fecha_nac)
    mail=input('Ingrese su mail: ')
    mail=valMail(mail)
    usuario=input('Escriba el nombre de usuario: ')
    usuario=validacionusuario(usuario,dicc1,dicc2)
    contrasena=input('Escriba una contrasena que contenga por lo menos una mayuscula y un numero: ')
    contrasena=validacioncontrasena(contrasena)
    return nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena

def valSignIn (dicc1:dict, dicc2:dict):
    validacion=True
    usuario=input('Ingrese su nombre de usuario: ')
    contrasena=input('Ingrese su contrasena: ')
    while validacion:
        if valPalabraDic(usuario,dicc1):
            cliente = dicc1.get(usuario)
            if cliente.contrasena == contrasena:
                validacion = False
            else:
                print('El nombre de usuario o su contraseña son incorrectos')
                usuario=input('Ingrese su nombre de usuario: ')
                contrasena=input('Ingrese su contrasena: ')
        elif valPalabraDic(usuario,dicc2):
            cliente=dicc2.get(usuario)
            if cliente.contrasena==contrasena:
                validacion=False
            else:
                print('El nombre de usuario o su contraseña son incorrectos')
                usuario=input('Ingrese su nombre de usuario: ')
                contrasena=input('Ingrese su contrasena: ')
        else:
            print('El nombre de usuario o su contraseña son incorrectos')
            usuario=input('Ingrese su nombre de usuario: ')
            contrasena=input('Ingrese su contrasena: ')
    return usuario, contrasena

def valTipoUsuario (usuario,dicc1:dict,dicc2:dict):
    if valPalabraDic (usuario,dicc1):
        cliente=True
        empleado=False
        tipo=None
    else:
        cliente=False
        empleado=dicc2.get(usuario)
        tipo=empleado.tipo
    return cliente,empleado,tipo

def valTipoEmpleado(tipo,dicc1:dict):
    while valPalabraDic(tipo,dicc1)==False:
        llaves=list(dicc1.keys())
        tipo=input('Error. Ese tipo de empleado no existe. \n Las opciones disponibles son: {} \n Ingrese una de las opciones existentes:'.format (llaves))
    return tipo

def valExiUsu (usuario,dicc1:dict):
    while valPalabraDic(usuario,dicc1)==False:
        usuario=input('Error. El nombre de usuario es inexistente. \n Ingrese el nombre de usuario: ')
    return usuario

def valOpcAsignacion(opcion,dicc1:dict,tipo,llave,imprimir):
    validar=False
    while validar==False: 
        if val_int(opcion)==False:
            for i, tareas in enumerate (dicc1[tipo][llave]):
                print (F"{i} - {tareas}")
            opcion=input('Error. Ingrese un número de la lista de opciones: ')
        opcion=int(opcion)
        opcion+=1
        if opcion>(len(dicc1[tipo][llave])):
            for i, tareas in enumerate (dicc1[tipo][llave]):
                print (F"{i} - {tareas}")
            opcion=input('Error. Ingrese un número de la lista de opciones: ')
        else:
            opcion-=1
            validar=True
            tarea=dicc1[tipo][llave][opcion]
    return tarea 

def valSiNo(eleccion,imprimir):
    while eleccion!='si' or eleccion!='no':
        eleccion=input(imprimir)
    if eleccion =='si':
        return True
    else:
        return False
    
def validacion_h(pregunta1, valor1, valor2):
    validacion = val_int(pregunta1)
    if validacion == True:
        if int(pregunta1) >= valor1 and int(pregunta1) <= valor2:
            habitacion = int(pregunta1)
        else:
            validacion = False
    return validacion
    
def validacion_preg_hab():
    pregunta = input('Elija una de las siguientes habitaciones: \n 1. Simple ($5000 - $15000) \n 2. Doble ($20000 - $30000) \n 3. Suite ($35000 - $45000) \n')
    imprimir = 'Error. Elija una de las siguientes habitaciones: \n 1. Simple ($5000 - $15000) \n 2. Doble ($20000 - $30000) \n 3. Suite ($35000 - $45000) \n'
    pregunta = val_opc(pregunta, 1, 3, imprimir)
    match pregunta:
        case 1:
            pregunta1 = input('Elija una de las siguientes opciones: \n 1: Sin baño privado y sin balcón ($5000) \n 2: Con baño y sin balcón ($10000) \n 3: Con baño privado y sin balcón ($10000) \n 4: Con baño privado y con balcón ($15000) \n')
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
        
def val_numres(numero, diccionario:dict(), nombre):
    validacion1=False
    validacion2=False
    while validacion1 == False or validacion2 == False:
        if val_int(numero):
            numero=int(numero)
            validacion1=True
            if valPalabraDic(numero, diccionario): 
                reserva = diccionario.get(numero) 
                persona = reserva.usuario
                if nombre == persona.usuario:
                    validacion2=True
                else:
                    print('Su numero de reserva es incorrecto')
                    numero = input('Ingrese su numero de reserva  ')
            else:
                    print('Su numero de reserva es incorrecto')
                    numero = input('Ingrese su numero de reserva  ')
        else: 
            numero = input('Error. Ingrese su numero de reserva  ')
    return numero
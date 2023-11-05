from datetime import *
from Habitacion_Doble import *
from Habitacion_Simple import *
from Habitacion_Suite import *
import numpy as np
from Tareas_Empleados import *
from Validaciones import *

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
    
    
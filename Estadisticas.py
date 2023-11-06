from Funciones import *
from Validaciones import *
from datetime import *
import numpy as np

def ordenar_fechas(lista):
    fechas_set = set(lista)
    fechas_lista = list(fechas_set)
    fechas_ordenadas=sorted(fechas_lista)
    return fechas_ordenadas

def val_preg(preg, lista,quiero):
    val = False
    while val == False:
        if quiero == 2:
            preg = convertirfecha_datetime(preg)
            preg = preg.date()
            print(preg)
        else:
            preg = convertirfecha_datetime(preg)
        if preg not in lista:
            preg = input('Error. Introduzca la fecha que desea ver: ')
        else:
            val = True
    return preg

def obtener_rango_fec(lista):
    todas = []
    for rango in lista:
        fecs = [rango[0], rango[1]]
        while fecs[0] <= fecs[1]:
            todas.append(fecs[0])
            fecs[0] += timedelta(days=1)
    return (todas)

def separacion_tipohab(lista):
    t1=[]
    t2=[]
    t3=[]
    for habitacion in lista:
        if habitacion.precio <= 15000:
            for estadia in habitacion.reservas:
                t1.append(estadia)
        elif habitacion.precio >= 35000:
            for estadia in habitacion.reservas:
                t3.append(estadia)
        else:
            for estadia in habitacion.reservas:
                t2.append(estadia)
    return t1, t2, t3

def preg_ver_estadisticas(ordenadas, imp, quiero):
    print(imp)
    for fecha in ordenadas:
        print(fecha.strftime('%d/%m/%Y'))
    preg = input('Introduzca la fecha que desea ver: ')
    fec = val_preg(preg, ordenadas,quiero)
    return fec
    
def imprimir_fec(lista,imp):
    fechas = []
    for habitacion in lista:
        if len(habitacion.reservas) != 0:
            for estadia in habitacion.reservas:
                fechas.append(estadia)
    desordenadas = obtener_rango_fec(fechas)
    desordenadas = np.array(desordenadas)
    ordenadas = ordenar_fechas(desordenadas)
    fec = preg_ver_estadisticas(ordenadas, imp,1)
    return fec, desordenadas

def ocupacion (lista):
    oc = 0
    for hab in lista:
        if len(hab.reservas) != 0:
            oc+=1
    if oc == 0:
        pass
    else:
        imp = 'Las fechas en las que hay reservas y puede ver la ocupación del hotel son las siguientes: '
        fec, desordenadas = imprimir_fec(lista, imp)
        conthab = np.count_nonzero(desordenadas == fec)
        porcentaje = (conthab / len(lista))*100
        return ('La ocupacion del hotel el dia {} es del {}% \n \n'.format(fec.strftime('%d/%m/%Y'), porcentaje))

def ocupacion_tipohab(lista):
    oc = 0
    for hab in lista:
        if len(hab.reservas) != 0:
            oc+=1
    if oc == 0:
        pass
    else:
        imp = 'Las fechas en las que hay reservas y puede ver la ocupación por tipo de habitación del hotel son las siguientes: '
        fec,desordenas = imprimir_fec(lista, imp)
        mat = np.array([])
        t1,t2,t3 = separacion_tipohab(lista)
        t1 = np.array(obtener_rango_fec(t1))
        t2 = np.array(obtener_rango_fec(t2))
        t3 = np.array(obtener_rango_fec(t3))
        mat = np.append(mat, [1,np.count_nonzero(t1 == fec)])
        mat = np.vstack((mat,[2,np.count_nonzero(t2 == fec)]))
        mat = np.vstack((mat,[3,np.count_nonzero(t3 == fec)]))
        todo = ('El dia {}: \n La ocupacion del tipo de habitacion simple es {}% \n La ocupacion del tipo de habitacion doble es {}% \n La ocupacion del tipo de habitacion doble es {}% \n \n'. format(fec.strftime('%d/%m/%Y'), ((mat[0][1])/4)*100, ((mat[1][1])/4)*100, ((mat[2][1])/4)*100))
        return todo

def rec_diaria(array):
    if len(array) == 0:
        print('El hotel no recaudacion aún')
        return
    else:
        imp = 'Los día que se realizaron gastos en el hotel son: '
        fechas = []
        for cobro in array:
            fechas.append(cobro.fecha.date())
        fechas = ordenar_fechas(fechas)
        dia = preg_ver_estadisticas(fechas, imp,2)
        rec = 0
        for cobro in array:
            if cobro.fecha.date() == dia:
                rec += cobro.monto
        return ('La recaudacion diaria el dia {} fue de ${}'.format(dia.strftime('%d/%m/%Y'), rec))

def ver_estadisticas_txt(lista, array):
    ocupa = ocupacion (lista)
    ocupa_th = ocupacion_tipohab(lista)
    rec = rec_diaria(array)
    try:
        with open('Estadisticas.txt', "w") as archivo:
            archivo.write(ocupa)
            archivo.write(ocupa_th)
            archivo.write(rec)
    except Exception:
        pass

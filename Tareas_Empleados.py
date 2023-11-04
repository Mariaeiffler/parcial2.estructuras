
tareas_empleados = {
    'cocina': {'empleados':[],'tareas':["Lavar los platos",'Cocinar desayuno',"Cocinar merienda","Cocinar cena"]},
    'limpieza': {'empleados':[],'tareas':["Limpieza de las habitaciones 1-3","Limpieza de las habitaciones 4-6",'Limpieza de las habitaciones 7-9',"Limpieza de las habitaciones 10-12"]},
    'mantenimiento':{'empleados':[],'tareas':['Mantenimiento de habitación','Mantenimiento de espacio común','Limpieza de pileta','Cortar el pasto']},
    'administrativo': {'empleados':[],'tareas':['Atender la recepcion','Mandar a lavar las toallas y la ropa de cama','Ayudar a los huespedes con sus preguntas','Ayudar a los huespedes a seleccionar actividades para realizar','Atender las quejas y preocupaciones de los clientes', 'Organizacion de eventos para huespedes','Coordinar servicios de transporte para los huespedes']},
    'gerente': {'empleados':[],'tareas':['Asignar tareas']}
}
    
def val_int(x): #valida que sea un entero
        try:
            num=int(x)
            return True
        except Exception:
            return False

#agregar para que asignen valor de importancia 
# generar metodo en hotel donde el servidor ppl pueda agregar mas tareas al diccionario de tareas

def valOpcAsignacion(opcion,dicc1:dict,tipo,llave,imprimir):
    validar=False
    while validar==False: 
        if val_int(opcion)==False:
            for i, tareas in enumerate (dicc1[tipo][llave]):
                print (F"{i} - {tareas}")
            opcion=input('Error. Ingrese un número de la lista de opciones: ')
        opcion=int(opcion)+1
        if opcion>(len(dicc1[tipo][llave])):
            for i, tareas in enumerate (dicc1[tipo][llave]):
                print (F"{i} - {tareas}")
            opcion=input('Error. Ingrese un número de la lista de opciones: ')
        else:
            validar=True
            tarea=dicc1[tipo][llave][opcion]
    return tarea 

if __name__ == '__main__':
    opc=input('opcion')
    opcion=valOpcAsignacion(opc,tareas_empleados,'cocina','tareas','NO')
    print(opcion)
    
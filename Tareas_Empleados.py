tareas_empleados = {
    'cocina': {'empleados':[],'tareas':["Lavar los platos",'Cocinar desayuno',"Cocinar merienda","Cocinar cena"]},
    'limpieza': {'empleados':[],'tareas':["Limpieza de las habitaciones 1-3","Limpieza de las habitaciones 4-6",'Limpieza de las habitaciones 7-9',"Limpieza de las habitaciones 10-12"]},
    'mantenimiento':{'empleados':[],'tareas':['Mantenimiento de habitación','Mantenimiento de espacio común','Limpieza de pileta','Cortar el pasto']},
    'administrativo': {'empleados':[],'tareas':['Atender la recepcion','Mandar a lavar las toallas y la ropa de cama','Ayudar a los huespedes con sus preguntas','Ayudar a los huespedes a seleccionar actividades para realizar','Atender las quejas y preocupaciones de los clientes', 'Organizacion de eventos para huespedes','Coordinar servicios de transporte para los huespedes']},
    'gerente': {'empleados':[],'tareas':['Asignar tareas']}
}

def agregarTareas (diccionario): #comprobar que sea administrador quien agregue la tarea
    tipo = input('Ingrese a que tipo de empleado desea agregarle la tarea: ')
    while tipo not in tareas_empleados:
        tipo = input ('No existe este tipo de empleados, ingrese el tipo de vuelta: ')
    tarea= input('Ingrese la tarea que desea agregar: ')
    diccionario[tipo].append(tarea)
    print ('La nueva tarea se ha  agregado con exito.')
    
def agregarTipoEmpleado (diccionario):
    tipo = input ('ingrese el nuevo tipo de empleado: ')
    while tipo in diccionario:
        tipo = input ('Error, ese tipo de empleado ya existe. Ingrese otro tipo de empleado: ')
    tarea = input ('Ingrese una tarea que realizaría este tipo de empleado: ')
    diccionario[tipo]= tarea
    print ('El tipo de empleado fue agregado con exito.')
    


#agregar para que asignen valor de importancia 
# generar metodo en hotel donde el servidor ppl pueda agregar mas tareas al diccionario de tareas

if __name__ == '__main__':
    cocina = tareas_empleados.get('cocina')
    print(cocina)
    tareas_empleados['cocina']['empleados'].append('hola')
    print(tareas_empleados['cocina'])
    tareas_empleados['cocina']['empleados'].remove('hola')
    print(tareas_empleados['cocina'])
    # lista = cocina.get('empleados')
    # lista.append('hola')
    # lista.remove('hola')
    # print(cocina)
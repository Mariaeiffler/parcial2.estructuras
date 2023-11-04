tareas_empleados = {
    'cocina': {'empleados':[],'tareas':["Lavar los platos",'Cocinar desayuno',"Cocinar merienda","Cocinar cena"]},
    'limpieza': {'empleados':[],'tareas':["Limpieza de las habitaciones 1-3","Limpieza de las habitaciones 4-6",'Limpieza de las habitaciones 7-9',"Limpieza de las habitaciones 10-12"]},
    'mantenimiento':{'empleados':[],'tareas':['Mantenimiento de habitación','Mantenimiento de espacio común','Limpieza de pileta','Cortar el pasto']},
    'administrativo': {'empleados':[],'tareas':['Atender la recepcion','Mandar a lavar las toallas y la ropa de cama','Ayudar a los huespedes con sus preguntas','Ayudar a los huespedes a seleccionar actividades para realizar','Atender las quejas y preocupaciones de los clientes', 'Organizacion de eventos para huespedes','Coordinar servicios de transporte para los huespedes']},
    'gerente': {'empleados':[],'tareas':['Asignar tareas']}
}
    


#agregar para que asignen valor de importancia 
# generar metodo en hotel donde el servidor ppl pueda agregar mas tareas al diccionario de tareas

if __name__ == '__main__':
    tipo='cocina'
    tipo=tareas_empleados.keys()
    print (tipo)
    
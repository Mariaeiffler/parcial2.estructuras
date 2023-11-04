class Comida():
    def __init__(self, descripcion, precio, tipo):
        self.descripcion = descripcion
        self.precio = precio
        self.tipo = tipo
        
    def __str__(self):
        return('Se pidio {}, que vale $ {} para {}'.format(self.descripcion, self.precio, self.tipo))
    
infusion= Comida('Infusión (Café con leche/Té/Jugo de Naranja)', 500, 'desayuno')
tostadas=Comida('Tostadas con queso y mermelada', 700, 'desayuno')
yogur=Comida('Yogur con cereales', 600, 'desayuno')
huevos_revueltos=Comida('Huevos revueltos', 800, 'desayuno')
facturas=Comida('Facturas',600, 'desayuno')
ensalada_frutas= Comida('Ensalada de frutas',750, 'desayuno')
pollo_carne=Comida('Pollo/Carne con guarnición', 2000, 'almuerzo')
sopa=Comida('Sopa del día', 1500, 'almuerzo')
ensalada=Comida('Ensalada 4 toppings', 1000, 'almuerzo')
pez=Comida('Pesca del dia', 3000, 'almuerzo')
opcion_vegetariana=Comida('Opción vegetariana (hamburguesa de lentejas con papas fritas)',1500, 'almuerzo')
pastas=Comida('Pastas (ravioles, ñoquis, sorrentinos)', 1500,'almuerzo')
postres=Comida('Postres (flan con dulce de leche, bocha de helado, tiramisú)',500,'almuerzo')
salmon=Comida('Salmón a la parrilla con puré de papas',4000,'cena')
pastas_cena= Comida('Pastas (ravioles, ñoquis, sorrentinos)',1500, 'cena')
opcion_vegetariana_cena=Comida('Opción vegetariana (falafel)',1500,'cena')
pizza=Comida('Pizza (muzzarella, napolitana, fugazzeta, calabresa)',2000, 'cena')
empanadas=Comida('Empanadas (carne, pollo, jamón y queso, verdura)',600,'cena')
asado_para_2=Comida('Asado con papas fritas (para 2)', 3000, 'cena')
asado_para_1=Comida('Asado con papas fritas (para 1)', 2000, 'cena')
postre_cena=Comida('Postres (flan con dulce de leche, bocha de helado, tiramisú)',500, 'cena')

print(infusion)



# un diccionario que se llame buffet en el que las claves sean los tipos y los valores sean los diccionarios de cada comida (desayuno, almuerzo, cena) 
# buffet= {'desayuno': diccionario_desayuno, 'almuerzo': diccionario_almuerzo, 'cena': diccionario_cena} 
# desayuno= {'1': infusion, '2': tostadas, '3': yogur, '4': huevos_revueltos, '5': facturas, '6': ensalada_frutas}
# almuerzo= {'1': pollo_carne, '2': sopa, '3': ensalada, '4': pez, '5': opcion_vegetariana, '6': pastas, '7': postres}
# cena= {'1': salmon, '2': pastas_cena, '3': opcion_vegetariana_cena, '4': pizza, '5': empanadas, '6': asado_para_2, '7': asado_para_1, '8': postre_cena}



for i in enumerate (buffet_dicc['desayuno']):
    print (i)
    


# def valOpcAsignacion(opcion,dicc1:dict,tipo,llave,imprimir):
#     validar=False
#     while validar==False: 
#         val_int(opcion)==False or opcion>len(dicc1[tipo][opcion][llave])-1
#         for i, tareas in enumerate (dicc1[tipo][llave]):
#             print (F"{i} - {tareas}")
#         opcion=input(imprimir)
#         opcion=int(opcion)
#     return opcion 
    
# if __name__=='__main__':
#     llaves=list(tareas_empleados.keys())
#     tipo=input('{} \n Ingrese el tipo de personal al que le quiere asignar una tarea: '.format(llaves))
#     tipo=valTipoEmpleado(tipo,tareas_empleados)
#     for i, tareas in enumerate (tareas_empleados[tipo]['tareas']):
#         print (F"{i} - {tareas}")
#     imprimir1='Ingrese la tarea que desea asignar: '
#     opcion=input(imprimir1)
#     opcion=valOpcAsignacion(opcion,tareas_empleados,tipo,'tareas',imprimir1)   
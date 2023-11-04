class Comida():
    def __init__(self, descripcion, precio, tipo,codigo):
        self.descripcion = descripcion
        self.precio = precio
        self.tipo = tipo
        self.codigo=codigo
        
    def __str__(self):
        if self.tipo!=None: 
            return('{}, que vale $ {} para {}'.format(self.descripcion, self.precio, self.tipo))
        else:
            return('{}, que vale $ {}'.format(self.descripcion, self.precio))
            
    
infusion= Comida('Infusión (Café con leche/Té/Jugo de Naranja)', 500, 'desayuno',1)
tostadas=Comida('Tostadas con queso y mermelada', 700, 'desayuno',2)
# yogur=Comida('Yogur con cereales', 600, 'desayuno')
# huevos_revueltos=Comida('Huevos revueltos', 800, 'desayuno')
# facturas=Comida('Facturas',600, 'desayuno')
# ensalada_frutas= Comida('Ensalada de frutas',750, 'desayuno')
# pollo_carne=Comida('Pollo/Carne con guarnición', 2000, 'almuerzo')
# sopa=Comida('Sopa del día', 1500, 'almuerzo')
# ensalada=Comida('Ensalada 4 toppings', 1000, 'almuerzo')
# pez=Comida('Pesca del dia', 3000, 'almuerzo')
# opcion_vegetariana=Comida('Opción vegetariana (hamburguesa de lentejas con papas fritas)',1500, 'almuerzo')
# pastas=Comida('Pastas (ravioles, ñoquis, sorrentinos)', 1500,'almuerzo')
# postres=Comida('Postres (flan con dulce de leche, bocha de helado, tiramisú)',500,'almuerzo')
# salmon=Comida('Salmón a la parrilla con puré de papas',4000,'cena')
# pastas_cena= Comida('Pastas (ravioles, ñoquis, sorrentinos)',1500, 'cena')
# opcion_vegetariana_cena=Comida('Opción vegetariana (falafel)',1500,'cena')
# pizza=Comida('Pizza (muzzarella, napolitana, fugazzeta, calabresa)',2000, 'cena')
# empanadas=Comida('Empanadas (carne, pollo, jamón y queso, verdura)',600,'cena')
# asado_para_2=Comida('Asado con papas fritas (para 2)', 3000, 'cena')
# asado_para_1=Comida('Asado con papas fritas (para 1)', 2000, 'cena')
# postre_cena=Comida('Postres (flan con dulce de leche, bocha de helado, tiramisú)',500, 'cena')
# bebida=Comida('Bebida a elección',500,None)

# diccionario_desayuno= [infusion,tostadas,yogur,huevos_revueltos,facturas,ensalada_frutas]
# diccionario_almuerzo= [pollo_carne,sopa,ensalada,pez,opcion_vegetariana,pastas,postres]
# diccionario_cena=[salmon,pastas_cena,opcion_vegetariana_cena,pizza,empanadas,asado_para_2,asado_para_1,postre_cena]
# buffet_dicc={'desayuno':diccionario_desayuno, 'almuerzo': diccionario_almuerzo, 'cena': diccionario_cena}
buffet_dicc={'desayuno':[infusion,tostadas]}
# for keys,values in buffet_dicc.values():
#     print(keys,values)

    

for i in enumerate (buffet_dicc['desayuno']):
    print(i)
    
    
    
#def valOpcAsignacion(opcion,dicc1:dict,tipo,llave,imprimir):
#     validar=False
#     while validar==False: 
#         val_int(opcion)==False or opcion>len(dicc1[tipo][opcion][llave])-1:
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
            
            


i=input('introduzca el codigo')
l=buffet_dicc.get('desayuno')
for objeto in l:
    if objeto.codigo==int(i):
        p=objeto.precio
        print(p)
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


    
infusion= Comida('Infusión (Café con leche/Té/Jugo de Naranja)', 500, 'desayuno','d1')
tostadas=Comida('Tostadas con queso y mermelada', 700, 'desayuno','d2')
yogur=Comida('Yogur con cereales', 600, 'desayuno','d3')
huevos_revueltos=Comida('Huevos revueltos', 800, 'desayuno','d4')
facturas=Comida('Facturas',600, 'desayuno','d5')
ensalada_frutas= Comida('Ensalada de frutas',750, 'desayuno','d6')
pollo_carne=Comida('Pollo/Carne con guarnición', 2000, 'almuerzo','d7')
sopa=Comida('Sopa del día', 1500, 'almuerzo','a1')
ensalada=Comida('Ensalada 4 toppings', 1000, 'almuerzo','a2')
pez=Comida('Pesca del dia', 3000, 'almuerzo','a3')
opcion_vegetariana=Comida('Opción vegetariana (hamburguesa de lentejas con papas fritas)',1500, 'almuerzo','a4')
pastas=Comida('Pastas (ravioles, ñoquis, sorrentinos)', 1500,'almuerzo','a5')
postres=Comida('Postres (flan con dulce de leche, bocha de helado, tiramisú)',500,'almuerzo','a6')
salmon=Comida('Salmón a la parrilla con puré de papas',4000,'cena','c1')
pastas_cena= Comida('Pastas (ravioles, ñoquis, sorrentinos)',1500, 'cena','c2')
opcion_vegetariana_cena=Comida('Opción vegetariana (falafel)',1500,'cena','c3')
pizza=Comida('Pizza (muzzarella, napolitana, fugazzeta, calabresa)',2000, 'cena','c4')
empanadas=Comida('Empanadas (carne, pollo, jamón y queso, verdura)',600,'cena','c5')
asado_para_2=Comida('Asado con papas fritas (para 2)', 3000, 'cena','c6')
asado_para_1=Comida('Asado con papas fritas (para 1)', 2000, 'cena','c7')
postre_cena=Comida('Postres (flan con dulce de leche, bocha de helado, tiramisú)',500, 'cena','c8')
bebida=Comida('Bebida a elección',500,None,'b')

diccionario_desayuno= [infusion,tostadas,yogur,huevos_revueltos,facturas,ensalada_frutas]
diccionario_almuerzo= [pollo_carne,sopa,ensalada,pez,opcion_vegetariana,pastas,postres]
diccionario_cena=[salmon,pastas_cena,opcion_vegetariana_cena,pizza,empanadas,asado_para_2,asado_para_1,postre_cena]
buffet_dicc={'desayuno':diccionario_desayuno, 'almuerzo': diccionario_almuerzo, 'cena': diccionario_cena,'bebida':bebida}

d=buffet_dicc.get('desayuno')
for objeto in d:
    print(objeto.codigo,objeto.descripcion,objeto.precio)
a=buffet_dicc.get('almuerzo')
for objeto in a:
    print(objeto.codigo,objeto.descripcion,objeto.precio)
c=buffet_dicc.get('cena')
for objeto in c:
    print(objeto.codigo,objeto.descripcion,objeto.precio)
b=buffet_dicc.get('bebida')
print(bebida.codigo,bebida.descripcion,bebida.precio)

pedido=input('Introduzca el codigo de lo que desea pedir:')

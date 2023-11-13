

class Comida():
    def __init__(self, descripcion, precio, tipo, numero):
        self.descripcion = descripcion
        self.precio = precio
        self.tipo = tipo
        self.numero=numero
        
    def __str__(self):
        if self.tipo!=None: 
            return('{}, que vale $ {} para {}'.format(self.descripcion, self.precio, self.tipo))
        else:
            return('{}, que vale $ {}'.format(self.descripcion, self.precio))
        
    def crear_comidas(): 
        ''' Esta funcion crea las comidas con su respectivo precio y codigo, especificando a que tipo de comida pertenece'''
        infusion= Comida('Infusión (Café con leche/Té/Jugo de Naranja)', 500, 'desayuno','1')
        tostadas=Comida('Tostadas con queso y mermelada', 700, 'desayuno','2')
        yogur=Comida('Yogur con cereales', 600, 'desayuno','3')
        huevos_revueltos=Comida('Huevos revueltos', 800, 'desayuno','4')
        facturas=Comida('Facturas',600, 'desayuno','5')
        ensalada_frutas= Comida('Ensalada de frutas',750, 'desayuno','6')
        pollo_carne=Comida('Pollo/Carne con guarnición', 2000, 'almuerzo','7')
        sopa=Comida('Sopa del día', 1500, 'almuerzo','8')
        ensalada=Comida('Ensalada 4 toppings', 1000, 'almuerzo','9')
        pez=Comida('Pesca del dia', 3000, 'almuerzo','10')
        opcion_vegetariana=Comida('Opción vegetariana (hamburguesa de lentejas con papas fritas)',1500, 'almuerzo','11')
        pastas=Comida('Pastas (ravioles, ñoquis, sorrentinos)', 1500,'almuerzo','12')
        postres=Comida('Postres (flan con dulce de leche, bocha de helado, tiramisú)',500,'almuerzo','13')
        tacos=Comida('Tacos varios (3 unidades)', 3000, 'almuerzo','14')
        salmon=Comida('Salmón a la parrilla con puré de papas',4000,'cena','15')
        pastas_cena= Comida('Pastas (ravioles, ñoquis, sorrentinos)',1500, 'cena','16')
        opcion_vegetariana_cena=Comida('Opción vegetariana (falafel)',1500,'cena','17')
        pizza=Comida('Pizza (muzzarella, napolitana, fugazzeta, calabresa)',2000, 'cena','18')
        empanadas=Comida('Empanadas (carne, pollo, jamón y queso, verdura)',600,'cena','19')
        asado_para_2=Comida('Asado con papas fritas (para 2)', 3000, 'cena','20')
        postre_cena=Comida('Postres (flan con dulce de leche, bocha de helado, tiramisú)',500, 'cena','21')
        bebida=Comida('Bebida a elección',500,None,'22')
        return infusion,tostadas,yogur,huevos_revueltos,facturas,ensalada_frutas,pollo_carne,sopa,ensalada,pez,opcion_vegetariana,pastas,postres,tacos,salmon,pastas_cena,opcion_vegetariana_cena,pizza,empanadas,asado_para_2,postre_cena,bebida
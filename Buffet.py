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
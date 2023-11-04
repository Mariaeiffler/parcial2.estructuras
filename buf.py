def mostrar_menu():
    print("Menú buffet:")
    print("1. Desayuno")
    print("2. Almuerzo")
    print("3. Cena")

def menu_desayuno():
    print("\nDesayuno:")
    opcion = input("Selecciona una opción de desayuno (1-6): ")
    match opcion:
        case "1":
            "Infusión (Café con leche/Té/Jugo de Naranja) - $500"
            pedido= pedido_buffet('Infusión')
        case "2":
            "Tostadas con queso y mermelada - $700"
            pedido= pedido_buffet('Tostadas')
        case "3":
            "Yogur con cereales - $600"
            pedido= pedido_buffet('Yogur')
        case '4':
            'Huevos revueltos - $800'
            pedido= pedido_buffet('Huevos Revueltos')
        case '5':
            'Facturas - $600'
            pedido= pedido_buffet('Facturas')
        case '6':
            'Ensalada de frutas - $750'
            pedido= pedido_buffet('Ensalada de frutas')
        case _:
            "Opción no válida"

    print(opcion)

def menu_almuerzo():
    print("\nAlmuerzo:")
    opcion = input("Selecciona una opción de almuerzo (1-7): ")
    match opcion:
        case "1":
            "Pollo/Carne con guarnición - $2000"
            pedido= pedido_buffet('Pollo/carne')
        case "2":
            "Sopa del día - $1500"
            pedido= pedido_buffet('Sopa')
        case "3":
            "Ensalada 4 toppings - $1000"
            pedido= pedido_buffet('Ensalada')
        case '4':
            'Pesca del día- $3000'
            pedido= pedido_buffet('Pesca del día')
        case '5':
            'Opción vegetariana (hamburguesa de lentejas con papas fritas)- $1500'
            pedido= pedido_buffet('Opción vegetariana')
        case '6':
            'Pastas (ravioles, ñoquis, sorrentinos)- $1500'
            pedido= pedido_buffet('Pastas')
        case '7':
            'Postres (flan con dulce de leche, bocha de helado, tiramisú)- $500 (c/u)'
            pedido= pedido_buffet('Postres')
        case _:
            "Opción no válida"

    print(opcion)

def menu_cena():
    print("\nCena:")
    opcion = input("Selecciona una opción de cena (1-7): ")
    match opcion:
        case "1":
            "Salmón a la parrilla con puré de papas - $4000"
            pedido= pedido_buffet('Salmón')
        case "2":
            "Pastas (ravioles, ñoquis, sorrentinos)- $1500"
            pedido= pedido_buffet('Pastas')
        case "3":
            'Opción vegetariana (falafel) - $1500'
            pedido= pedido_buffet('Opción vegetariana')
        case '4':
            'Pizza (muzzarella, napolitana, fugazzeta, calabresa) - $2000)'
            pedido= pedido_buffet('Pizaa')
        case '5':
            'Empanadas (carne, pollo, jamón y queso, verdura) - $600 (c/u))'
            pedido= pedido_buffet('Empanadas')
        case '6':
            'Asado con papas fritas - $3000 (para 2 personas) (se puede pedir para 1 persona por $2000)'
            pedido= pedido_buffet('Asado')
        case '7':
            'Postres (flan con dulce de leche, bocha de helado, tiramisú)- $500 (c/u)'
            pedido= pedido_buffet('Postres')
        case _:
            "Opción no válida"

    print(opcion)

def main():
    while True:
        mostrar_menu()
        opcion_comida = input("Selecciona una comida del día (1 para desayuno/merienda, 2 para almuerzo, 3 para cena, listo para salir): ")

        match opcion_comida:
            case "1":
                menu_desayuno()
            case "2":
                menu_almuerzo()
            case "3":
                menu_cena()
            case "listo":
                break
            case _:
                print("Opción no válida. Por favor, selecciona una comida válida.")

def pedido_buffet(pedido):
    cola=[]
    cola.insert(0,pedido)
    return cola

# def terminar_pedido():
#     self.cola.pop()


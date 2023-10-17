def validacionpregunta(pregunta):
    if pregunta != 1 or pregunta != 2:
        pregunta = input('Elija una de las siguientes opciones: 1. Sign up \n 2. Sign in  ')
        while pregunta != 1 or pregunta != 2:
            pregunta = input('Elija una de las siguientes opciones: 1. Sign up \n 2. Sign in  ')
    return pregunta
        
def validaciondni(dni):
    if str(dni).isdigit() == False or len(str(dni)) != 8:
        dni = input('Ingrese su DNI  ')
        while str(dni).isdigit() == False or len(str(dni)) != 8:
            dni = input('Ingrese su DNI  ')
    ## agregar tambien que no se repita
    return dni

def validacioncontraseña1(contraseña):
    mayuscula = False
    numero = False
    for digito in contraseña:
        if digito.isdigit() == True:
            numero = True
        if digito.isupper() == True:
            mayuscula = True
    return mayuscula, numero

def validacioncontraseña2(contraseña):
    mayuscula, numero = validacioncontraseña1(contraseña)
    if mayuscula == False or numero == False:
        contraseña = input ('Ingrese una contraseña valida ')
        mayuscula, numero = validacioncontraseña1(contraseña)
        while mayuscula == False or numero == False:
            contraseña = input ('Ingrese una contraseña valida ')
            mayuscula, numero = validacioncontraseña1(contraseña)
        return contraseña
    verificacion = True
    return verificacion

def validacionempleado(soy_empleado):
    if soy_empleado != 'si' or soy_empleado != 'no':
        print ('hola')
        soy_empleado = input('Ingrese si, si es empleado y no si no lo es (en minuscula) ')
        while soy_empleado != 'si' or soy_empleado != 'no':
            print ('chau')
            soy_empleado = input('Ingrese si, si es empleado y no si no lo es (en minuscula) ')
    if soy_empleado == 'si':
        return True
    else:
        return False

soy_empleado = 'si'
validacion = validacionempleado(soy_empleado)






##########################################  ARCHIVOS

# import csv

# def abrirArchivo(archivo):
#     lista = []
#     try:
#         with open(archivo, 'r', encoding='utf-8') as archivo:
#             lector = csv.reader(archivo)                       
#             for fila in lector:                        
#                 lista.append(fila)
#         return (lista)
        
#     except FileNotFoundError:
#         print("El archivo", 'FILE', "no existe.")
#     return

# try:
#     fn = input('Ingrese el nombre del archivo a abrir: ')
#     fd = None
#     fd = open( fn , 'r')
#     line = fd.readline()
# except FileNotFoundError:
#     print('El archivo no existe. Ingrese otro archivo.')
# finally:
#     if fd:
#         print('cerrando el archivo')
#         fd.close()


# def leer_archivo( fn ):
#     fd = open( fn , 'r' )
#     cont = fd.read()
#     fd.close()
#     return cont

# def escribir_archivo( fname , contenido ):
#     fd = open( fname , 'w' )
#     for linea in contenido:
#         fd.write(' '.join(linea)+'\n')
#     fd.close()
    
# with open('FILE', 'r', encoding='utf-8') as archivo:   # 1
#   lector = csv.reader(archivo)                       # 2
#   for fila in lector:                                # 3
#     las_capitales.append(fila)
# print(las_capitales) 

# try: # Probamos el siguiente código
#     with open('FILE', 'r', encoding='utf-8') as archivo:
#         lector = csv.reader(archivo)
#         for fila in lector:
#             las_capitales.append(fila)
    
# except FileNotFoundError:  # Si se encuentra un error se ejecuta esta parte
#     print("El archivo", 'FILE', "no existe.")
    
# else: # De no encontrarse ningún error luego del bloque try continuamos en el else
#     print(las_capitales) 


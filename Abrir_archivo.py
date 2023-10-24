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

# def escribir_archivo( fname , contenido ): #appendea cosas al final
#     fd = open( fname , 'a' )
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
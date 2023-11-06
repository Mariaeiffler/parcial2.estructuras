# from datetime import *
# from Habitacion_Doble import *
# from Habitacion_Simple import *
# from Habitacion_Suite import *
# import numpy as np
# from Tareas_Empleados import *
# from Funciones import cantidad_numero
# from Funciones import convertirfecha_datetime
# from Funciones import mayoredad
# from Funciones import valPalabraDic
# from Funciones import cantidad_mayusculas

# def val_int(x): #valida que sea un entero
#         try:
#             num=int(x)
#             return True
#         except Exception:
#             return False
        
# def val_opc(opcion, valor1, valor2, imprimir): #valida las opciones del menu ppl
#     validacion=False
#     while validacion == False:
#         if val_int(opcion):
#             x=int(opcion)
#             if x in range(valor1, valor2+1):
#                 validacion=True
#             else:
#                 opcion = input(imprimir)
#         else: 
#             opcion = input(imprimir)
#     return x

# def valNombre1(nombre):
#     validacion = True
#     for digito in nombre:
#         if digito.isalpha() == False and digito.isspace() == False:
#             validacion = False
#     return validacion
    
# def valNombre2 (nombre):
#     validacion = valNombre1(nombre)
#     while validacion == False:
#         nombre = input('Ingrese su nombre y apellido: ')
#         validacion = valNombre1(nombre)
#     return nombre

# def validaciondni(dni,dic1:dict,dic2:dict): 
#     vali1 = False
#     vali2 = False
#     while vali1 == False or vali2 == False:
#         while str(dni).isdigit() == False or len(str(dni)) != 8:
#             dni = input('Ingrese su DNI  ')
#         if len(dic1) != 0:
#             for cliente in dic1:
#                 if dic1.get(cliente).dni == dni:
#                     dni = input('El DNI ingresado ya pertenece a otro usuario. Ingrese nuevamente su DNI  ')
#                 else:
#                     vali1 = True
#         else:
#             vali1 = True
#         if len(dic2) != 0:
#             for emp in dic2:
#                 if dic2.get(emp).dni == dni:
#                     dni = input('El DNI ingresado ya pertenece a otro usuario. Ingrese nuevamente su DNI  ')
#                 else:
#                     vali2 = True
#         else:
#             vali2 = True
#     return dni

# def validacioncontacto(contacto):
#     while cantidad_numero(contacto) != len(str(contacto)) or cantidad_numero(contacto) != 13:
#         contacto = input('Ingrese su numero de telefono con el formato 54911... ')
#     return contacto

# def validacionfechanac (fecha): # --> no la toque 
#     fecha_datetime = convertirfecha_datetime(fecha)
#     if mayoredad(fecha_datetime) == False:
#         fecha = input('Ingrese la fecha en el formato dd/mm/yyyy: ')
#         fecha_datetime = convertirfecha_datetime(fecha)
#         while mayoredad(fecha_datetime) == False:
#             fecha = input('Ingrese la fecha en el formato dd/mm/yyyy: ')
#             fecha_datetime = convertirfecha_datetime(fecha)
#     return fecha_datetime

# def valMail (mail):
#     while mail.count('@')!=1 or mail.count('.')<1:
#         mail=input('Error. Ingrese su mail (tiene que contener por lo menos un . y un @):')
#     return mail

# def validacionusuario(usuario,dic1,dic2): #TODO:chequear que no este repetido
#     while len(str(usuario)) < 5 or valPalabraDic(usuario,dic1) or valPalabraDic(usuario,dic2):
#         usuario = input('Ingrese otro nombre de usuario válido (con minimo 5 dígitos): ')  
#     return usuario

# def validacioncontrasena(contrasena): 
#     while cantidad_mayusculas(contrasena) < 1  or cantidad_numero(contrasena) <1:
#         contrasena = input ('Ingrese una contraseña valida, que contenga una mayuscula y un numero: ')
#     return contrasena

# def infoPersonas (dicc1:dict,dicc2:dict):   
#     nombre=input('Introduzca su nombre y apellido: ')
#     nombre=valNombre2(nombre)
#     dni=input('Ingrese su DNI: ')
#     dni=validaciondni(dni, dicc1, dicc2)
#     direccion=input('Ingrese su direccion: ')
#     contacto=input('Ingrese su numero de contacto: ')
#     contacto=validacioncontacto(contacto)
#     fecha_nac=input('Ingrese su fecha de nacimiento: (Debe ser mayor de edad para crearse un usuario) ')
#     fecha_nac=validacionfechanac (fecha_nac)
#     mail=input('Ingrese su mail: ')
#     mail=valMail(mail)
#     usuario=input('Escriba el nombre de usuario: ')
#     usuario=validacionusuario(usuario,dicc1,dicc2)
#     contrasena=input('Escriba una contrasena que contenga por lo menos una mayuscula y un numero: ')
#     contrasena=validacioncontrasena(contrasena)
#     return nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena

# def valSignIn (dicc1:dict, dicc2:dict):
#     validacion=True
#     usuario=input('Ingrese su nombre de usuario: ')
#     contrasena=input('Ingrese su contrasena: ')
#     while validacion:
#         if valPalabraDic(usuario,dicc1):
#             cliente = dicc1.get(usuario)
#             if cliente.contrasena == contrasena:
#                 validacion = False
#             else:
#                 print('El nombre de usuario o su contraseña son incorrectos')
#                 usuario=input('Ingrese su nombre de usuario: ')
#                 contrasena=input('Ingrese su contrasena: ')
#         elif valPalabraDic(usuario,dicc2):
#             cliente=dicc2.get(usuario)
#             if cliente.contrasena==contrasena:
#                 validacion=False
#             else:
#                 print('El nombre de usuario o su contraseña son incorrectos')
#                 usuario=input('Ingrese su nombre de usuario: ')
#                 contrasena=input('Ingrese su contrasena: ')
#         else:
#             print('El nombre de usuario o su contraseña son incorrectos')
#             usuario=input('Ingrese su nombre de usuario: ')
#             contrasena=input('Ingrese su contrasena: ')
#     return usuario, contrasena

# def valTipoUsuario (usuario,dicc1:dict,dicc2:dict):
#     if valPalabraDic (usuario,dicc1):
#         cliente=True
#         empleado=False
#         tipo=None
#     else:
#         cliente=False
#         empleado=dicc2.get(usuario)
#         tipo=empleado.tipo
#     return cliente,empleado,tipo

# def valTipoEmpleado(tipo,dicc1:dict):
#     while valPalabraDic(tipo,dicc1)==False:
#         llaves=list(dicc1.keys())
#         tipo=input('Error. Ese tipo de empleado no existe. \n Las opciones disponibles son: {} \n Ingrese una de las opciones existentes:'.format (llaves))
#     return tipo

# def valExiUsu (usuario,dicc1:dict):
#     while valPalabraDic(usuario,dicc1)==False:
#         usuario=input('Error. El nombre de usuario es inexistente. \n Ingrese el nombre de usuario: ')
#     return usuario

# def valOpcAsignacion(opcion,dicc1:dict,tipo,llave,imprimir):
#     validar=False
#     while validar==False: 
#         if val_int(opcion)==False:
#             for i, tareas in enumerate (dicc1[tipo][llave]):
#                 print (F"{i} - {tareas}")
#             opcion=input('Error. Ingrese un número de la lista de opciones: ')
#         opcion=int(opcion)
#         opcion+=1
#         if opcion>(len(dicc1[tipo][llave])):
#             for i, tareas in enumerate (dicc1[tipo][llave]):
#                 print (F"{i} - {tareas}")
#             opcion=input('Error. Ingrese un número de la lista de opciones: ')
#         else:
#             opcion-=1
#             validar=True
#             tarea=dicc1[tipo][llave][opcion]
#     return tarea 

# def valSiNo(eleccion,imprimir):
#     while eleccion!='si' or eleccion!='no':
#         eleccion=input(imprimir)
#     if eleccion =='si':
#         return True
#     else:
#         return False
    
# def validacion_h(pregunta1, valor1, valor2):
#     validacion = val_int(pregunta1)
#     if validacion == True:
#         if int(pregunta1) >= valor1 and int(pregunta1) <= valor2:
#             habitacion = int(pregunta1)
#         else:
#             validacion = False
#     return validacion
    
# def validacion_preg_hab():
#     pregunta = input('Elija una de las siguientes habitaciones: \n 1. Simple ($5000 - $15000) \n 2. Doble ($20000 - $30000) \n 3. Suite ($35000 - $45000) \n')
#     imprimir = 'Error. Elija una de las siguientes habitaciones: \n 1. Simple ($5000 - $15000) \n 2. Doble ($20000 - $30000) \n 3. Suite ($35000 - $45000) \n'
#     pregunta = val_opc(pregunta, 1, 3, imprimir)
#     match pregunta:
#         case 1:
#             pregunta1 = input('Elija una de las siguientes opciones: \n 1: Sin baño privado y sin balcón ($5000) \n 2: Con baño y sin balcón ($10000) \n 3: Con baño privado y sin balcón ($10000) \n 4: Con baño privado y con balcón ($15000) \n')
#             validacion = validacion_h(pregunta1,1, 4)
#             while(validacion == False):
#                 pregunta1 = input('Elija una de las siguientes opciones: \n 1: Sin baño privado y sin balcón ($5000) \n 2: Con baño y sin balcón ($10000) \n 3: Con baño privado y sin balcón ($10000) \n 4: Con baño privado y con balcón ($15000)  \n')
#                 validacion = validacion_h(pregunta1,1,4)
#             return pregunta1
#         case 2:
#             pregunta1 = input('Elija una de las siguientes opciones: \n 5: Sin baño privado y sin balcón ($20000) \n 6: Con baño y sin balcón ($25000) \n 7: Con baño privado y sin balcón ($25000) \n 8: Con baño privado y con balcón ($30000) \n')
#             validacion = validacion_h(pregunta1,5,8)
#             while(validacion == False):
#                 pregunta1 = input('Elija una de las siguientes opciones: \n 5: Sin baño privado y sin balcón ($20000) \n 6: Con baño y sin balcón ($25000) \n 7: Con baño privado y sin balcón ($25000) \n 8: Con baño privado y con balcón ($30000) \n')
#                 validacion = validacion_h(pregunta1,5,8)
#             return pregunta1
#         case 3:
#             pregunta1 = input('Elija una de las siguientes opciones: \n 9: Sin baño privado y sin balcón ($35000) \n 10: Con baño y sin balcón ($40000) \n 11: Con baño privado y sin balcón ($40000) \n 12: Con baño privado y con balcón ($45000) \n')
#             validacion = validacion_h(pregunta1,9,12)
#             while(validacion == False):
#                 pregunta1 = input('Elija una de las siguientes opciones: \n 9: Sin baño privado y sin balcón ($35000) \n 10: Con baño y sin balcón ($40000) \n 11: Con baño privado y sin balcón ($40000) \n 12: Con baño privado y con balcón ($45000) \n')
#                 validacion = validacion_h(pregunta1,9,12)
#             return pregunta1
        
# def val_numres(numero, diccionario:dict(), nombre):
#     validacion1=False
#     validacion2=False
#     while validacion1 == False or validacion2 == False:
#         if val_int(numero):
#             numero=int(numero)
#             validacion1=True
#             if valPalabraDic(numero, diccionario): 
#                 reserva = diccionario.get(numero) 
#                 persona = reserva.usuario
#                 if nombre == persona.usuario:
#                     validacion2=True
#                 else:
#                     print('Su numero de reserva es incorrecto')
#                     numero = input('Ingrese su numero de reserva  ')
#             else:
#                     print('Su numero de reserva es incorrecto')
#                     numero = input('Ingrese su numero de reserva  ')
#         else: 
#             numero = input('Error. Ingrese su numero de reserva  ')
#     return numero
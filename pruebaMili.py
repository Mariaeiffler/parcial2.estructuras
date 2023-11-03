from prueba_menu import *
from Hotel_prueba import *

def valPalabraDic (palabra,dicc:dict):
    if palabra in dicc:
        return True
    else:
        return False

# si es empleado: empleado=True Tipo=tipo cliente = false
# Si es cliente: cliente=true tipo=none empleado=false 
def valTipoUsuario (usuario,dicc1:dict,dicc2:dict):
    if valPalabraDic (usuario,dicc1):
        cliente=True
        empleado=False
        tipo=None
    else:
        cliente=False
        empleado=dicc2.get(usuario)
        tipo=cliente.tipo
    return cliente,empleado,tipo
        
        
        



def valSignIn (dicc1:dict, dicc2:dict):
    validacion=True
    usuario=input('Ingrese su nombre de usuario: ')
    contrasena=input('Ingrese su contrasena: ')
    while validacion:
        if valPalabraDic(usuario,dicc1):
            cliente = dicc1.get(usuario)
            if cliente.contrasena == contrasena:
                validacion = False
            else:
                print('El nombre de usuario o su contraseña son incorrectos')
                usuario=input('Ingrese su nombre de usuario: ')
                contrasena=input('Ingrese su contrasena: ')
        elif valPalabraDic(usuario,dicc2):
            cliente=dicc2.get(usuario)
            if cliente.contrasena==contrasena:
                validacion=False
            else:
                print('El nombre de usuario o su contraseña son incorrectos')
                usuario=input('Ingrese su nombre de usuario: ')
                contrasena=input('Ingrese su contrasena: ')
        else:
            print('El nombre de usuario o su contraseña son incorrectos')
            usuario=input('Ingrese su nombre de usuario: ')
            contrasena=input('Ingrese su contrasena: ')
            
    return usuario, contrasena
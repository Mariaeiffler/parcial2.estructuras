def entrar():
    pregunta=input('Elija una de las siguientes opciones: 1. Sign up \n 2.Sign in')
    #validacion 
    match pregunta:
        case 1:
            #validar que no exista el usuario
            #validar todos los atributos
            nombre=input('Introduzca su nombre:')
            dni=input('Ingrese su DNI:')
            direccion=input('Ingrese su direccion:')
            contacto=input('Ingrese su numero de contacto:')
            fecha_nac=input('Ingrese su fecha de nacimiento:')
            mail=input('Ingrese su mail:')
            usuario=input('Escriba el nombre de usuario:')
            contrasena=input('Escriba la contrasena:')
            soy_empleado=input('Sos empleado?')
            
            
        case 2:
            #validar que exista el usuario y que la contrasena sea correcta
            usuario=input('Escriba el nombre de usuario:')
            contrasena=input('Escriba la contrasena:')
            

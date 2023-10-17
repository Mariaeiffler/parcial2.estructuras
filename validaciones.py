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



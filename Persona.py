
class Persona():
    def __init__(self,nombre,usuario,dni,contacto,fecha_nac,mail,contrasena):
        self.nombre=nombre
        self.dni=dni
        self.contacto=contacto
        self.fecha_nac=fecha_nac
        self.mail=mail
        self.usuario=usuario
        self.contrasena=contrasena
        
# creo q se podria borrar:
        
    def _str_(self):
        cadena=''
        cadena='La persona llamada {}, nacio el {}, tiene DNI {}, la informacion de contacto es {}, el mail es {}, su usuario es {}'.format(self.nombre,self.fecha_nac,self.dni,self.contacto,self.mail,self.usario)
        return cadena
    
    def _eq_(self, personita): #es necesario?
        if id(self)==id(personita):
             return True
        elif self.ident==personita.ident:
                return True
        else:  return False
        


        
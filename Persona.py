class Persona():
    def _init_(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,contrasena): #el true es de personal
        self.nombre=nombre
        self.dni=dni
        self.direccion=direccion
        self.contacto=contacto
        self.fecha_nac=fecha_nac
        self.mail=mail
        self.usuario=usuario
        self.contrasena=contrasena
        
    def _str_(self):
        cadena=''
        cadena='La persona llamada {}, nacio el {}, tiene DNI {}, su direccion es {}, la informacion de contacto es {}, el mail es {}, su usuario es {}'.format(self.nombre,self.fecha_nac,self.dni,self.direccion,self.contacto,self.mail,self.usario)
        return cadena
    
    def _eq_(self, personita): #es necesario?
        if id(self)==id(personita):
             return True
        elif self.ident==personita.ident:
                return True
        else:  return False
        
if __name__ == "__main__":
    persona=Persona('Carlos',12345678,'vakjijw',12345432,12/34/12,'oreifoie',True)

        
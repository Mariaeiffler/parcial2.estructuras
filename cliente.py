from Persona import Persona
class Cliente(Persona):
    def __init__(self,nombre,dni,direccion,contacto,fecha_nac,mail):
        super().__init__(nombre,dni,direccion,contacto,fecha_nac,mail)
    #def tipo(self):
        #verificar que tipo de cliente es en base a sus gastos
    #def historial_reservas(self):
    #def __str__(self):
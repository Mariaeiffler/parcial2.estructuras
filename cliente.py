from Persona import Persona
class Cliente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,soy_empleado,contrasena,tipo='nivel 1', reservas = []):
        super().__init__(nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado)
        self.usuario = usuario
        self.contrasena = contrasena
        self.tipo=tipo
        self.reservas= reservas
        
    #def tipo(self):
        #verificar que tipo de cliente es en base a sus gastos
        
    #def historial_reservas(self):
    
    #def realizar_pedido_buffet():
    
    #def __str__(self):
    
    #def tipocliente(self):
from Persona import Persona
from Buffet import *

class Cliente(Persona):
    def __init__(self,nombre,usuario,dni,direccion,contacto,fecha_nac,mail,soy_empleado,contrasena,tipo='nivel 1', reservas = []):
        super().__init__(nombre,dni,direccion,contacto,fecha_nac,mail,soy_empleado)
        self.usuario = usuario
        self.contrasena = contrasena
        self.tipo=tipo
        self.reservas= reservas
    
    def realizar_pedido():
        Buffet.self.mostrar_menu()
    
    #aca hay que traer los metodos de buffet para que el cliente pueda hacer los pedidos y
    # en la clase personal, el cocinero debería hacer el pedido. 
    # Una vez que se hace un pedido, se debería agregar a las tareas del personal de cocina. 
    
        
        
        
    #def tipo(self):
        #verificar que tipo de cliente es en base a sus gastos
        
    #def historial_reservas(self):
    
    #def realizar_pedido_buffet():
    
    #def __str__(self):
    
    #def tipocliente(self)
    
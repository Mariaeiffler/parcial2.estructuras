from collections import deque

class Pila():
    def __init__(self):
        self.pila=deque()
        
    def apilar (self,elemento):
        self.pila.append(elemento)
    
    def desapilar (self):
        if len(self.pila)>0:
            return self.pila.pop()
        else:
            return None
    
    def obtenerUltimo (self):
        if len(self.pila)>0:
            return self.pila[-1]
        

        
if __name__ == "__main__":
    pila=Pila()
    pila.apilar('hola')
    pila.apilar('chau')
    pila.apilar('agus')
    pila.apilar('ampi')
    print(pila.obtenerUltimo())
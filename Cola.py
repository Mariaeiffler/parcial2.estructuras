class Cola():
    def __init__(self):
        self.cola = []

    def esta_vacia(self):
        '''Esta funcion devuelve True si la cola esta vacia, sino False'''
        return len(self.cola) == 0

    def encolar(self, item):
        '''Esta funcion anade un elemento a la cola'''
        self.cola.append(item)
        return

    def desencolar(self):
        '''Esta funcion quita un elemento de la cola'''
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            return None
    
    def mostrarPrimero (self):
        '''Esta funcion devuelve el primer elemento de la cola'''
        if self.esta_vacia():
            return None
        else:
            return self.cola[0]
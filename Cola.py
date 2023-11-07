class Cola():
    def __init__(self):
        self.cola = []

    def esta_vacia(self):
        return len(self.cola) == 0

    def encolar(self, item):
        self.cola.append(item)
        return

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            return None
    
    def mostrarPrimero (self):
        if self.esta_vacia():
            return None
        else:
            return self.cola[0]
class Cola():
    def __init__(self):
        self.cola = []
    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)
        return

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None
    
    def mostrarPrimero (self):
        if self.esta_vacia():
            return None
        else:
            primero=self.cola[1]

class NodoTarea:
    def __init__(self, valor, importancia):
        self.valor = valor
        self.importancia=importancia
        self.prox = None
    def __str__(self)->str:
       return str(self.valor)
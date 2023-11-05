from nodo import NodoTarea
class Lista_Enlazada():
    def __init__(self):  
        self.head= None
        self.len=0
    
    def agregarInicio (self,nodo:NodoTarea):
        if (self.len==0): 
            self.head=nodo
        else:
            nodo.prox=self.head  
            self.head=nodo 
        self.len+=1
        
    def __str__(self): 
        nodo=self.head 
        cadena=''
        if self.len==0:
            return "No tiene tareas por hacer"
        else:
            while (nodo!=None):
                cadena+=str(nodo.valor)+'\t' 
                nodo=nodo.prox
            return cadena 
        
    def append (self,nodo:NodoTarea): 
        if self.len==0:
            self.head=nodo
        else:
            nodomov=self.head
            while nodomov.prox!=None: 
                nodomov=nodomov.prox 
            nodomov.prox=nodo
        self.len+=1

    def agregarNodoTarea(self, nuevoNodo: NodoTarea):
        if self.len == 0:
            self.head = nuevoNodo
        elif nuevoNodo.importancia < self.head.importancia:
            nuevoNodo.prox = self.head
            self.head = nuevoNodo
        else:
            nodoMov = self.head
            while nodoMov.prox and nuevoNodo.importancia >= nodoMov.prox.importancia:
                nodoMov = nodoMov.prox
            nuevoNodo.prox = nodoMov.prox
            nodoMov.prox = nuevoNodo
        self.len += 1
        
    def eliminarPrimero(self):
        if self.head:
            self.head = self.head.prox
        else:
            print("La lista está vacía. No hay elementos para eliminar.")

            
            
if __name__ == '__main__':
    lista=Lista_Enlazada()
    nodo1=NodoTarea('12',1)
    lista.append(nodo1)
    nodo2=NodoTarea('Las m',2)
    lista.append(nodo2)
    nodo3=NodoTarea('hola',1)
    lista.agregarNodoTarea(nodo3)
    lista.eliminarPrimero()
    print(lista.__str__())
    
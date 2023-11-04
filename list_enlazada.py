from nodo import NodoTarea
class Lista_Enlazada():
    def __init__(self):  
        self.inicio= None
        self.len=0
        
    def is_empty(self):
        return self.head is None
    
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
            return "lista es vacia"
        else:
            while (nodo!=None):
                cadena+=str(nodo.dato)+'\t' 
                nodo=nodo.prox
            return cadena 
        
    def append (self,nodo:NodoTarea): 
        if self.len==0:
            self.head=nodo
        else:
            nodomov=NodoTarea()
            nodomov=self.head
            while nodomov.prox!=None: 
                nodomov=nodomov.prox 
            nodomov.prox=nodo
        self.len+=1
        
    def pop(self,posicion=None): 
        nodo=NodoTarea()
        nodo=self.head
        if posicion == None: 
            final=self.len-2
            for i in range (final): 
                nodo=nodo.prox
            nodo.prox=None 
        else: 
            for i in range (posicion-1):
                nodo=nodo.prox
            nodo.prox=nodo.prox.prox 
        self.len=-1
        
    def eliminarPorValor (self,valor): 
        if self.is_empty():
            return
        if self.head.dato == valor:
            self.head = self.head.prox
            return
        current = self.head
        while current.prox:
            if current.prox.dato == valor:
                current.prox = current.prox.prox
                return
            current = current.prox
    
    def nodoSiguiente (self,nodo:NodoTarea):
        if self.is_empty():
            return 'La lista está vacía'
        else:
            nodoProx=nodo.prox
            return nodoProx
        
    def appendDespVal (self,valor,nodo:NodoTarea): 
        nuevoNodo=nodo
        if self.is_empty():
            self.head=nuevoNodo
        else:
            nodoAct=self.head
            while nodoAct:
                if self.head.dato==valor:
                    nuevoNodo.prox=nodoAct.prox
                    nodoAct.prox=nuevoNodo
                    return
                nodoAct=nodoAct.prox
                
    def combListas (self,lista2): #Ej 3
            listaFinal=Lista_Enlazada()
            nodo_act_lista1=self.head
            nodo_act_lista2=lista2.head
            while nodo_act_lista1 or nodo_act_lista2:
                if nodo_act_lista1:
                    listaFinal.append(nodo_act_lista1)
                    nodo_act_lista1=nodo_act_lista1.prox
                if nodo_act_lista2:
                    listaFinal.append(nodo_act_lista2)
                    nodo_act_lista2=nodo_act_lista2.prox
            return listaFinal
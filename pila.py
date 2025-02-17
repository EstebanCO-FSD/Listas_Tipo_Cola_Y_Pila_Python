# Lista tipo pila

from nodo import Nodo

class Pila:

    def __init__(self):
        self.cima = None

    def apilar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cima is not None:
            nuevo_nodo.siguiente = self.cima
        
        self.cima = nuevo_nodo

    def desapilar(self):
        if self.cima is None:
            return None
        
        dato_desapilado = self.cima.dato
        self.cima = self.cima.siguiente

        return dato_desapilado
    
    def obtenerElementos(self):
        lista = []
        actual = self.cima

        while actual:
            lista.append(actual.dato)
            actual = actual.siguiente

        return lista
    
    def cantidadElementosPares(self):
        lista = self.obtenerElementos()
        pares = 0

        for i in lista:
            if i % 2 == 0:
                pares += 1

        return pares
    
    def promedioElementos(self):
        lista = self.obtenerElementos()
        
        if lista:
            return sum(lista) / len(lista)

        return 0
    
    def ultimoElemento(self):
        if self.cima:
            return self.cima.dato
        else:
            return None
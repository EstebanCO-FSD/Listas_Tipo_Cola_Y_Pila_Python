# Lista tipo cola

from nodo import Nodo

class Cola:

    def __init__(self):
        self.inicio = None
        self.fin = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.fin is not None:
            self.fin.siguiente = nuevo_nodo

        self.fin = nuevo_nodo

        if self.inicio is None:
            self.inicio = nuevo_nodo

    def eliminar(self):
        if self.inicio is None:
            return None
        
        dato_eliminado = self.inicio.dato
        self.inicio = self.inicio.siguiente

        if self.inicio is None:
            self.fin = None

        return dato_eliminado
    
    def obtenerElementos(self):
        lista = []
        actual = self.inicio

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
        if self.fin:
            return self.fin.dato
        else:
            return None
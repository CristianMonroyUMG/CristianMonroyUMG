'''
Implementar una pila utilizando una lista en Python.
Crear funciones para realizar las operaciones básicas de una pila: push (añadir elemento), pop (eliminar elemento) y peek (ver el elemento superior sin eliminarlo).
Escribir un programa que utilice esta pila para invertir el orden de una lista dada.
Implementación de una Cola (Queue):
'''

#Se define la clase para la implementación de la cola Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
lista_original = []

#Ingresar valores a la lista original con .append
lista_original.append(1)
lista_original.append(2)
lista_original.append(3)
lista_original.append(4)
lista_original.append(5)

#Se define la función peek con sus especificaciones.
def peek(lista_P):
    if len(lista_P) > 0:
        return lista_P[0]
    else:
        return None

#Se imprime el primer elemento de la lista origintal.
primer_elemento = peek(lista_original)
print("Primer elemento de la lista:",primer_elemento,"\n")

def revertir_lista(lista):
    pila = []
    lista_revertida = []
    for elemento in lista:
        pila.append(elemento)
#Hay que extraer datos de la pila para incorporarlos en la lista revertida.
#While para que realice el proceso de extraer y añadir de todos los elementos.
    while pila:
        lista_revertida.append(pila.pop())
    return lista_revertida

#Se le aplica la función revertir_lista a lista_original.
lista_revertida = revertir_lista(lista_original)

print("Lista original:",lista_original,"\n")
print("Lista revertida:",lista_revertida,"\n")
'''
Escribir una función que tome una cola y revierta la mitad de sus elementos utilizando solo una pila 
adicional. La cola debe mantener la misma secuencia de elementos, pero la mitad debe estar en orden inverso
'''

from collections import deque

def revertir_mitad_cola(cola):
    pila = []
   #Verificar si la cola está vacía o tiene un solo elemento.
    if len(cola) <= 1:
        return cola
    
    #Encolar la primera mitad en la pila.
    mitad = len(cola) // 2
    for _ in range(mitad):
        pila.append(cola.popleft())

    #Desencolar y encolar desde la pila para invertir la primera mitad.
    while pila:
        cola.append(pila.pop())

    #Encolar la segunda mitad nuevamente en la cola.
    for _ in range(mitad):
        cola.append(cola.popleft())

    return cola

cola = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("\nCola original:",cola)
revertir_mitad_cola(cola)
print("\nCola con la mitad de valores invertidos:",cola,"\n")


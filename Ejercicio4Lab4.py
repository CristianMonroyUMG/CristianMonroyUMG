'''
Desarrollar una clase ColaConPilas que utilice dos pilas para simular el comportamiento de una cola.
Implementar las operaciones enqueue y dequeue utilizando las operaciones de pilas.
'''

class ColaConPilas:
    def __init__(self):
        self.pila_entrada = []
        self.pila_salida = []

    def enqueue(self, elemento):
        #Añadir los elementos a la pila de entrada.
        self.pila_entrada.append(elemento)

    def dequeue(self):
        # Verificar si la pila de salida está vacía.
        if not self.pila_salida:
            # Si está vacía, transferir los elementos de la pila de entrada a la pila de salida.
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())

        # Si la pila de salida aún está vacía entonces la cola está vacía e imprimirá None.
        if not self.pila_salida:
            return None  

        # Retornar el elemento de la pila de salida (que representa el primer elemento en la cola).
        return self.pila_salida.pop()

#Hacemos uso de la clase ColaConPilas para implementar sus funciones.
cola = ColaConPilas()

cola.enqueue('a')
cola.enqueue('b')
cola.enqueue('c')
cola.enqueue('d')

print("Salida #1:",cola.dequeue())  
print("Salida #2:",cola.dequeue())  
print("Salida #3:",cola.dequeue())  
print("Salida #4:",cola.dequeue())  
print("Salida #5:",cola.dequeue())  

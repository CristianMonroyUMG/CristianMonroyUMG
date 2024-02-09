'''
Definir funciones para las operaciones básicas de una cola: enqueue (añadir elemento), dequeue (eliminar 
elemento) y front (ver el primer elemento sin eliminarlo).
Escribir un programa que simule el proceso de atención en una fila, donde los elementos son atendidos en 
el orden en que llegan.
'''

from collections import deque
import time

def enqueue(self, item):
        self.items.append(item)

def dequeue(self):
    if not self.is_empty():
        return self.items.pop(0)
    else:
        return None

def front(self):
    if not self.is_empty():
        return self.items[0]
    else:
        return None

def simular_linea_espera(clientes):
    queue = deque(clientes) #Extraer o eliminar datos al inicio o al final de la cola (popleft)
    print("Orden de atención:",queue,"\n")
    
    while queue: #Mientras que la cola tenga el tamaño de los clientes...
        print("Atendiendo al cliente",queue.popleft())
        time.sleep(2)

#Clientes en espera...
clientes_en_espera = ["Josué","Lucas","Bethany","Sophia"]

#Atenderá a 4 clientes, simulando una lista de espera en un banco a 4 clientes.
print("\nUsted se encuentra en una fila, porfavor, espere su turno para ser atendido.")
simular_linea_espera(clientes_en_espera)

print("\nTodos los clientes han sido atendidos correctamente.")


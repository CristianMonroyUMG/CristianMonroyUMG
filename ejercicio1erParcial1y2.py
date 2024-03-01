
## Inciso 1 y 2
class Operaciones():
    def __init__(self):
        self.lista = [" Juan "," Julia "," Pedro "]
        self.cadena = "Python"

    def sumatoria_elementos(self, lista):
        suma = lista[0] + lista[1] + lista[2]
        return suma
    def inverso_palabra(self, cadena):
        cadena_invertida = cadena[::-1]
        return cadena_invertida

objeto = Operaciones()

listado = objeto.lista
cadenaIn = objeto.cadena

resultado = objeto.sumatoria_elementos(listado)
print("La suma de los elementos es de: ",resultado)

cadIn = objeto.inverso_palabra(cadenaIn)
print("La cadena invertida es:",cadIn)

    
'''
Escribir una función en Python que tome una cadena de paréntesis y determine si están balanceados.
Utilizar una pila para rastrear la apertura y cierre de paréntesis.
'''

def paréntesis_balanceados(cadena):
    pila = []
    #Definir las parejas de paréntesis con caracteres.
    parejas = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in parejas.values():
            pila.append(caracter)
        elif caracter in parejas.keys():
            if pila == [] or parejas[caracter] != pila.pop():
                return False
            #Ignorar otros caracteres que no sean paréntesis
            #Devolver True si la pila está vacía, False en caso contrario.
            return not pila 

#Cadenas para verficar si están balanceadas o no.
cadena1 = "((){)}"
cadena2 = "({[})"
cadena3 = "a(b)c[d]e"

print("¿La cadena",cadena1,"está balanceada?",paréntesis_balanceados(cadena1))  
print("¿La cadena",cadena2,"está balanceada?",paréntesis_balanceados(cadena2))  
print("¿La cadena",cadena3,"está balanceada?",paréntesis_balanceados(cadena3))  

print("\nTRUE SI LA SUMA ES PAR, FALSE SI LA SUMA ES IMPAR")

def suma_es_par(a, b):
    suma = a + b
    return suma % 2 == 0

num1 = int(input("\nIngrese un número: "))
num2 = int(input("Ingrese otro número: "))

resultado = suma_es_par(num1, num2)
print(resultado)

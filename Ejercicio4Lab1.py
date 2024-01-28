import math

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

raiz = b**2 - 4*a*c

if raiz >= 0:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)
    print("Las soluciones son x1 = ",x1," y x2 = ",x2,)
else:
    print("La ecuación cuadrática no tiene soluciones reales.")

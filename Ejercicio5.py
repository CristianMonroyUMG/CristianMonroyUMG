entero = input("Ingrese un número entero: ")
if entero.isdigit():
    entero = int(entero)
    print("Entero: ",entero)
else:
    print("Error: Ingrese un número entero válido.")
    exit(0)

flotante = input("Ingrese un número decimal: ")
if flotante.replace('.', '', 1).isdigit():
    flotante = float(flotante)
    print("Flotante: ",flotante)
else:
    print("Error: Ingrese un número decimal válido.")
    exit(0)

caracter = input("Ingrese un carácter: ")
if len(caracter) == 1:
    caracter = caracter
    print("Carácter: ",caracter)
else:
    print("Error: Debe ingresar un solo carácter para el tipo char.")
    exit(0)

cadena = input("Ingrese una cadena de texto: ")
print("Cadena: ",cadena)

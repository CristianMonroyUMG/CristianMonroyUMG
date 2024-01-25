valor = input("Ingrese un dato: ")

if valor.isdigit():
    tipo_dato = "entero"
elif valor.replace('.', '', 1).isdigit():
    tipo_dato = "flotante"
elif len(valor) == 1:
    tipo_dato = "carácter"
else:
    tipo_dato = "cadena"

print("El dato ingresado es de tipo",tipo_dato)


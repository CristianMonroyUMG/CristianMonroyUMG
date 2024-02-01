print("\nAPROBADO O REPROBADO")

class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def estado(self):
        return self.nota >= 60

nombreE = input("\nIngrese su nombre: ")
edadE = int(input("Ingrese su edad: "))
notaE = int(input("Ingrese su calificación: "))

estudiante1 = Estudiante(nombreE, edadE, notaE)

if estudiante1.estado():
    print(nombreE,"ha aprobado con",notaE,"puntos.") 
else:
    print(nombreE,"ha reprobado con",notaE,"puntos.")

import json

class AFD:
    def __init__(self, transiciones, estado_inicial, estados_aceptación, estados_finales_cadena):
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estado_actual = estado_inicial
        self.estados_aceptación = estados_aceptación
        self.estados_finales_cadena = estados_finales_cadena

    def resetear(self):
        """Resetea al estado inicial."""
        self.estado_actual = self.estado_inicial
    
    def validar_cadena(self, cadena_entrada):
        """Valida una cadena y muestra el recorrido."""
        self.resetear()
        recorrido = [self.estado_actual]
        for char in cadena_entrada:
            if char in self.transiciones[self.estado_actual]:
                self.estado_actual = self.transiciones[self.estado_actual][char]
                recorrido.append(self.estado_actual)
            else:
                print("Cadena no válida.")
                return False, recorrido
        if self.estado_actual in self.estados_aceptación or self.estado_actual in self.estados_finales_cadena:
            print("Cadena válida.")
            return True, recorrido
        else:
            print("Cadena no válida.")
            return False, recorrido

def crear_transiciones(estados, simbolos):
    """Solicita al usuario las transiciones para cada estado y símbolo."""
    transiciones = {}
    estados_finales_cadena = []
    for estado in estados:
        transiciones[estado] = {}
        for simbolo in simbolos:
            estado_destino = input(f"Con '{simbolo}' desde {estado}: ")
            if estado_destino.lower() == "error":
                continue  # No agrega una transición si se indica "Error"
            transiciones[estado][simbolo] = estado_destino
        # Pregunta si el estado actual es un estado final de cadena
        es_final_cadena = input(f"¿Es {estado} final de cadena? 0 (No) o 1 (Sí): ")
        if es_final_cadena == "1":
            estados_finales_cadena.append(estado)
    return transiciones, estados_finales_cadena

# Configuración del AFD
estados = ["q0", "q1", "q2", "q3", "q4", "q5", "q6"]
simbolos = ["+", "W", "-", "*", "vocal"]
estado_inicial = "q0"
estados_aceptación = ["q6"]  # Define los estados de aceptación según el diseño

# Crear el autómata
transiciones, estados_finales_cadena = crear_transiciones(estados, simbolos)
afd = AFD(transiciones, estado_inicial, estados_aceptación, estados_finales_cadena)

# Guardar la configuración del AFD en un archivo JSON
with open("transiciones.json", "w") as f:
    json.dump({
        "transiciones": transiciones,
        "estado_inicial": estado_inicial,
        "estados_aceptación": estados_aceptación,
        "estados_finales_cadena": estados_finales_cadena
    }, f)

print("Las transiciones y estados finales de cadena se han guardado en 'transiciones.json'.")

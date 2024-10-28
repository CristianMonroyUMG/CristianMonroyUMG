import json
from graphviz import Digraph

class AFD:
    def __init__(self, transiciones, estado_inicial, estados_aceptación, estados_finales_cadena):
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_aceptación = estados_aceptación
        self.estados_finales_cadena = estados_finales_cadena

    def validar_cadena(self, cadena_entrada):
        """Valida una cadena y muestra el recorrido completo por los estados."""
        estado_actual = self.estado_inicial
        recorrido = [estado_actual]
        
        for char in cadena_entrada:
            if char in self.transiciones[estado_actual]:
                estado_actual = self.transiciones[estado_actual][char]
                recorrido.append(estado_actual)
            else:
                print("Cadena no válida: transición no definida.")
                return False, recorrido
        
        # Verificar si el estado final es de aceptación o de cadena válida
        if estado_actual in self.estados_aceptación or estado_actual in self.estados_finales_cadena:
            print("Cadena válida.")
            return True, recorrido
        else:
            print("Cadena no válida: no terminó en un estado de aceptación o final de cadena.")
            return False, recorrido

def cargar_afd(ruta_archivo):
    """Carga el AFD desde un archivo JSON."""
    with open(ruta_archivo, "r") as f:
        datos = json.load(f)
    afd = AFD(
        datos["transiciones"],
        datos["estado_inicial"],
        datos["estados_aceptación"],
        datos["estados_finales_cadena"]
    )
    return afd

def visualizar_afd(afd):
    """Genera la visualización del AFD usando Graphviz."""
    dot = Digraph(comment="AFD", graph_attr={"rankdir": "LR"})  # Orientación horizontal
    
    # Estilos para los diferentes tipos de estados
    for estado in afd.transiciones.keys():
        if estado in afd.estados_aceptación and estado in afd.estados_finales_cadena:
            dot.node(estado, shape="doublecircle", style="filled", color="lightblue", label=f"{estado} (final y fin)")
        elif estado in afd.estados_aceptación:
            dot.node(estado, shape="doublecircle", color="green", label=f"{estado} (final)")
        elif estado in afd.estados_finales_cadena:
            dot.node(estado, shape="circle", style="filled", color="yellow", label=f"{estado} (fin)")
        else:
            dot.node(estado, shape="circle")
    
    # Agregar transiciones
    for estado, caminos in afd.transiciones.items():
        for simbolo, estado_destino in caminos.items():
            dot.edge(estado, estado_destino, label=simbolo)

    # Estado inicial
    dot.node("", shape="point")  # Nodo invisible para indicar el estado inicial
    dot.edge("", afd.estado_inicial)

    dot.render("afd_grafico", format="png", cleanup=True)
    print("La visualización del autómata se ha guardado como 'afd_grafico.png'.")

def main():
    # Cargar AFD desde el archivo JSON
    afd = cargar_afd("transiciones.json")

    # Visualizar AFD
    visualizar_afd(afd)

    # Validar una cadena ingresada por el usuario
    cadena_entrada = input("Ingrese una cadena para validar: ")
    es_valida, recorrido = afd.validar_cadena(cadena_entrada)
    print("Recorrido del autómata:", " -> ".join(recorrido))
    if es_valida:
        print("La cadena es válida para el autómata.")
    else:
        print("La cadena no es válida para el autómata.")

if __name__ == "__main__":
    main()

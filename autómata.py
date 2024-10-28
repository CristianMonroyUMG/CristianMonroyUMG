import json

class DFA:
    def __init__(self, transitions, start_state, accept_states):
        self.transitions = transitions
        self.current_state = start_state
        self.accept_states = accept_states
    
    def reset(self):
        """Resetea al estado inicial."""
        self.current_state = start_state
    
    def validate_string(self, input_string):
        """Valida una cadena y muestra el recorrido."""
        path = [self.current_state]
        for char in input_string:
            if char in self.transitions[self.current_state]:
                self.current_state = self.transitions[self.current_state][char]
                path.append(self.current_state)
            else:
                print("Cadena no válida.")
                return False, path
        if self.current_state in self.accept_states:
            print("Cadena válida.")
            return True, path
        else:
            print("Cadena no válida.")
            return False, path

def create_transitions(states, symbols):
    """Solicita al usuario las transiciones para cada estado y símbolo."""
    transitions = {}
    for state in states:
        transitions[state] = {}
        for symbol in symbols:
            target_state = input(f"Con '{symbol}' hacia {state}: ")
            if target_state.lower() == "error":
                continue  # No agrega una transición si se indica "Error"
            transitions[state][symbol] = target_state
    return transitions

# Configuración del DFA
states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6"]
symbols = ["+", "E", "-", "*", "digito"]
start_state = "q0"
accept_states = ["q6"]  # Define los estados de aceptación según el diseño

# Crear el autómata
transitions = create_transitions(states, symbols)
dfa = DFA(transitions, start_state, accept_states)

with open("transitions.json", "w") as f:
    json.dump(transitions, f)

print("Las transiciones se han guardado en 'transitions.json'.")
import tkinter as tk
import serial
import threading

# Configurar la conexión serie con Arduino
puerto = 'COM9'  # Cambiar esto al puerto correcto en tu sistema
ser = serial.Serial(puerto, 9600)

# Variable global para el canvas
canvas = None

# Definir la clase Nodo para el árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.circle_id = None  # Identificador del círculo en el canvas

# Crear un árbol de ejemplo
raiz = Nodo('R')
raiz.izquierda = Nodo('A')
raiz.derecha = Nodo('V')
raiz.izquierda.izquierda = Nodo('R')
raiz.izquierda.derecha = Nodo('V')

# Función para recorrer el árbol según el orden
def inorden(nodo):
    if nodo is not None:
        inorden(nodo.izquierda)
        print(nodo.valor, end=" ")
        inorden(nodo.derecha)

def posorden(nodo):
    if nodo is not None:
        posorden(nodo.izquierda)
        posorden(nodo.derecha)
        print(nodo.valor, end=" ")

def preorden(nodo):
    if nodo is not None:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierda)
        preorden(nodo.derecha)

# Función para actualizar la interfaz gráfica según el orden recibido
def actualizar_orden(orden):
    global raiz
    global canvas

    # Apagar los LEDs antes de comenzar un nuevo orden
    apagar_leds()

    # Actualizar el árbol según el orden recibido
    if orden == b'A':
        preorden(raiz)
        cambiar_color(orden)
    elif orden == b'B':
        inorden(raiz)
        cambiar_color(orden)
    elif orden == b'C':
        posorden(raiz)
        cambiar_color(orden)

# Función para cambiar el color de los círculos según el recorrido del árbol
def cambiar_color(orden):
    global canvas
    if orden == b'A':
        print("Preorden")
        canvas.itemconfig(raiz.preorden_id, fill="red")
        canvas.itemconfig(raiz.circle_id, fill="red")
        canvas.after(1000, lambda: canvas.itemconfig(raiz.izquierda.circle_id, fill="yellow"))
        canvas.after(2000, lambda: canvas.itemconfig(raiz.izquierda.izquierda.circle_id, fill="red"))
        canvas.after(3000, lambda: canvas.itemconfig(raiz.izquierda.derecha.circle_id, fill="green"))
        canvas.after(4000, lambda: canvas.itemconfig(raiz.derecha.circle_id, fill="green"))
        canvas.after(5000, apagar_leds)  # Apagar LEDs después de completar el recorrido

    elif orden == b'B':
        print("Inorden")
        canvas.itemconfig(raiz.inorden_id, fill="red")
        canvas.itemconfig(raiz.izquierda.izquierda.circle_id, fill="red")
        canvas.after(1000, lambda: canvas.itemconfig(raiz.izquierda.circle_id, fill="yellow"))
        canvas.after(2000, lambda: canvas.itemconfig(raiz.izquierda.derecha.circle_id, fill="green"))
        canvas.after(3000, lambda: canvas.itemconfig(raiz.circle_id, fill="red"))
        canvas.after(4000, lambda: canvas.itemconfig(raiz.derecha.circle_id, fill="green"))
        canvas.after(5000, apagar_leds)  # Apagar LEDs después de completar el recorrido

    elif orden == b'C':
        print("Postorden")
        canvas.itemconfig(raiz.postorden_id, fill="red")
        canvas.itemconfig(raiz.izquierda.izquierda.circle_id, fill="red")
        canvas.after(1000, lambda: canvas.itemconfig(raiz.izquierda.derecha.circle_id, fill="green"))
        canvas.after(2000, lambda: canvas.itemconfig(raiz.izquierda.circle_id, fill="yellow"))
        canvas.after(3000, lambda: canvas.itemconfig(raiz.derecha.circle_id, fill="green"))
        canvas.after(4000, lambda: canvas.itemconfig(raiz.circle_id, fill="red"))
        canvas.after(5000, apagar_leds)  # Apagar LEDs después de completar el recorrido

# Función para apagar los LEDs (restaurar color original de los círculos)
def apagar_leds():
    global raiz
    global canvas
    canvas.itemconfig(raiz.circle_id, fill="white")  # Restaurar color de la raíz
    canvas.itemconfig(raiz.izquierda.circle_id, fill="white")  # Restaurar color de la rama izquierda
    canvas.itemconfig(raiz.izquierda.izquierda.circle_id, fill="white")  # Restaurar color de la sub-rama izquierda
    canvas.itemconfig(raiz.izquierda.derecha.circle_id, fill="white")  # Restaurar color de la sub-rama derecha
    canvas.itemconfig(raiz.derecha.circle_id, fill="white")  # Restaurar color de la rama derecha

    canvas.itemconfig(raiz.preorden_id, fill="white") # cuadro de preorden
    canvas.itemconfig(raiz.inorden_id, fill="white") # cuadro de inorden
    canvas.itemconfig(raiz.postorden_id, fill="white") # cuadro de postorden

# Función para recibir datos del puerto serie
def recibir_datos(canvas, barra):  # Agregar barra como argumento
    while True:
        if ser.in_waiting > 0:
            datos = ser.readline().strip()
            if datos.startswith(b'P'):
                # Actualizar la altura de la barra en la interfaz gráfica
                cambiar_altura(canvas, barra, datos[1:])  # Pasar también barra como argumento
            else:
                # Actualizar el orden en la interfaz gráfica
                actualizar_orden(datos)

# Función para cambiar la altura de la barra en la interfaz gráfica
def cambiar_altura(canvas, barra, valor_potenciometro):
    try:
        altura = int(valor_potenciometro)
        altura_barra = (300 - altura) * 2  # Invertir la altura para que la barra crezca hacia arriba y dividir la escala entre 2 para que no se exceda en altura
        canvas.coords(barra, 450, altura_barra, 480, 700)
    except ValueError:
        print("Error al convertir los datos del potenciómetro a entero")

# Crear la interfaz gráfica
def draw():
    global canvas
    root = tk.Tk()
    root.title("Círculos con bordes")
    root.geometry("700x750")

    canvas = tk.Canvas(root, width=600, height=600)
    canvas.pack()

    barra = canvas.create_rectangle(450, 700, 480, 300, fill="blue", outline="black")

    # Dibujar círculos con bordes negros
    tk.Label(root, text="Arbol: ").place(x=50, y=50)
    tk.Label(root, text="Potenciómetro: ").place(x=420, y=50)

    raiz_circle = canvas.create_oval(160, 50, 210, 100, outline="black", fill="white")  # raiz
    rama_izq_circle = canvas.create_oval(70, 150, 120, 200, outline="black", fill="white")  # rama izquierda
    sub_rama_izq_circle = canvas.create_oval(10, 250, 60, 300, outline="black", fill="white")  # sub-rama izquierda
    sub_rama_der_circle = canvas.create_oval(140, 250, 190, 300, outline="black", fill="white")  # sub-rama izquierda
    rama_der_circle = canvas.create_oval(260, 150, 310, 200, outline="black", fill="white")  # rama derecha

    # Guardar referencias a los círculos en el árbol
    raiz.circle_id = raiz_circle
    raiz.izquierda.circle_id = rama_izq_circle
    raiz.izquierda.izquierda.circle_id = sub_rama_izq_circle
    raiz.izquierda.derecha.circle_id = sub_rama_der_circle
    raiz.derecha.circle_id = rama_der_circle

    preorden = canvas.create_rectangle(10, 400, 70, 360, outline="black")  # cuadro de preorden
    tk.Label(root, text="PreOrden").place(x=140, y=368)

    inorden = canvas.create_rectangle(10, 420, 70, 460, outline="black")  # cuadro de inorden
    tk.Label(root, text="InOrden").place(x=140, y=428)

    postorden = canvas.create_rectangle(10, 480, 70, 520, outline="black")  # cuadro de posorden
    tk.Label(root, text="PostOrden").place(x=140, y=488)

    # Guardar referencias a los recuadros de los órdenes
    raiz.preorden_id = preorden
    raiz.inorden_id = inorden
    raiz.postorden_id = postorden

    # Iniciar el hilo para recibir datos del puerto serie
    threading.Thread(target=recibir_datos, args=(canvas, barra)).start()

    root.mainloop()

# Ejecutar la función para dibujar la interfaz gráfica
draw()


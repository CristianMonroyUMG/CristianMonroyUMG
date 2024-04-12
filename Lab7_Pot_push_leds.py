import tkinter as tk
import serial
import threading


def draw():
    root = tk.Tk()
    root.title("Círculos con bordes")
    root.geometry("700x750")

    canvas = tk.Canvas(root, width=600, height=600)
    canvas.pack()

    barra = canvas.create_rectangle(450, 700, 480, 300, fill="blue", outline="black")


    def cambiar_altura(valor_potenciometro):
        try:
            altura = int(valor_potenciometro)
            altura_barra = (1200 - altura) / 2  # Invertir la altura para que la barra crezca hacia arriba y dividir la escala entre 2 para que no se exceda en altura
            canvas.coords(barra, 450, altura_barra, 480, 700)
            
        except ValueError:
            print("Error al convertir los datos del potenciómetro a entero")

    # Dibujar círculos con bordes negros
    tk.Label(root, text="Arbol: ").place(x=50, y=50)
    tk.Label(root, text="Potenciómetro: ").place(x=420,y=50)

    raiz = canvas.create_oval(160, 50, 210, 100, outline="black")  # raiz
    rama_izq = canvas.create_oval(70, 150, 120, 200, outline="black")  # rama izquierda
    sub_rama_izq = canvas.create_oval(10, 250, 60, 300, outline="black")  # sub-rama izquierda
    sub_rama_der = canvas.create_oval(140, 250, 190, 300, outline="black")  # sub-rama izquierda
    rama_der = canvas.create_oval(260, 150, 310, 200, outline="black")  # rama derecha

    preorden = canvas.create_rectangle(10, 400, 70, 360, outline="black") # cuadro de preorden
    tk.Label(root, text="PreOrden").place(x=140, y=368)

    inorden = canvas.create_rectangle(10, 420, 70, 460, outline="black") # cuadro de inorden
    tk.Label(root, text="InOrden").place(x=140, y=428)

    postorden = canvas.create_rectangle(10, 480, 70, 520, outline="black") # cuadro de posorden
    tk.Label(root, text="PostOrden").place(x=140, y=488)


    # Función para cambiar el color de los círculos según el orden
    def cambiar_color(data):
        if data == "A":
            print("PreOrden")
            canvas.itemconfig(preorden, fill="red")
            canvas.itemconfig(raiz, fill="red")
            root.after(1000, lambda: canvas.itemconfig(rama_izq, fill="yellow"))
            root.after(2000, lambda: canvas.itemconfig(sub_rama_izq, fill="red"))
            root.after(3000, lambda: canvas.itemconfig(sub_rama_der, fill="green"))
            root.after(4000, lambda: canvas.itemconfig(rama_der, fill="green"))
            root.after(5000, apagar_leds)  # Llamar a la función apagar_leds después de 2500 ms

        elif data == "B":
            print("InOrden")
            canvas.itemconfig(inorden, fill="red")
            canvas.itemconfig(sub_rama_izq, fill="red")
            root.after(1000, lambda: canvas.itemconfig(rama_izq, fill="yellow"))
            root.after(2000, lambda: canvas.itemconfig(sub_rama_der, fill="green"))
            root.after(3000, lambda: canvas.itemconfig(raiz, fill="red"))
            root.after(4000, lambda: canvas.itemconfig(rama_der, fill="green"))
            root.after(5000, apagar_leds)  # Llamar a la función apagar_leds después de 2500 ms

        elif data == "C":
            print("PostOrden")
            canvas.itemconfig(postorden, fill="red")
            canvas.itemconfig(sub_rama_izq, fill="red")
            root.after(1000, lambda: canvas.itemconfig(sub_rama_der, fill="green"))
            root.after(2000, lambda: canvas.itemconfig(rama_izq, fill="yellow"))
            root.after(3000, lambda: canvas.itemconfig(rama_der, fill="green"))
            root.after(4000, lambda: canvas.itemconfig(raiz, fill="red"))
            root.after(5000, apagar_leds)  # Llamar a la función apagar_leds después de 2500 ms

    # Función para restablecer el color de los círculos a su estado original (sin relleno)
    def apagar_leds():
        canvas.itemconfig(preorden, fill="")
        canvas.itemconfig(inorden, fill="")
        canvas.itemconfig(postorden, fill="")
        canvas.itemconfig(raiz, fill="")
        canvas.itemconfig(rama_izq, fill="")
        canvas.itemconfig(sub_rama_izq, fill="")
        canvas.itemconfig(sub_rama_der, fill="")
        canvas.itemconfig(rama_der, fill="")

    # Función para recibir datos de Arduino
    def recibir_datos():
        try:
            ser = serial.Serial('COM9', 9600) 
            while True:
                data = ser.readline().decode().strip()  # Leer los datos recibidos de Arduino
                cambiar_color(data)
                if data.startswith("P"):  # Verificar si los datos son del potenciómetro
                    valor_potenciometro = data[1:]  # Extraer el valor del potenciómetro
                    cambiar_altura(valor_potenciometro)  # Llamar a la función para cambiar la altura de la barra
        except serial.SerialException:
            print("Error de conexión serial")

    # Crear un hilo para ejecutar la función recibir_datos()
    thread = threading.Thread(target=recibir_datos)
    thread.daemon = True
    thread.start()

    root.mainloop()

# Llamar a la función draw() aquí.
draw()

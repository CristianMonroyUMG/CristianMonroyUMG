# Cristian Mariano Monroy Fernández 0901-22-16592

import serial
import tkinter as tk

# Establece la conexión serie con Arduino
ser = serial.Serial('COM9', 9600) 

# Función para enviar comandos a Arduino para encender o apagar LEDs
def control_leds(led_group):
    ser.write(led_group.encode())

# Función para cambiar el estado del botón y enviar comando a Arduino
def toggle_button(led_group):
    # Cambiar el estado del botón en la interfaz gráfica
    if buttons[led_group].cget("bg") == "white":
        buttons[led_group].config(bg="yellow")
        control_leds(led_group.upper())  # Encender LEDs en Arduino
    else:
        buttons[led_group].config(bg="white")
        control_leds(led_group.lower())  # Apagar LEDs en Arduino

# Función para cambiar el estado del cuadro de LEDs y encender o apagar LEDs correspondientes
def toggle_led(led_group):
    # Cambiar el estado del cuadro de LEDs en la interfaz gráfica
    if led_squares[led_group].cget("bg") == "red":
        led_squares[led_group].config(bg="green")
        control_leds(led_group.upper())  # Encender LEDs en Arduino
    else:
        led_squares[led_group].config(bg="red")
        control_leds(led_group.lower())  # Apagar LEDs en Arduino

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Control de LEDs")

# Define y muestra los cuadrados para representar los LEDs y push buttons
leds = ['A', 'B', 'C', 'D']
led_squares = {}
button_squares = {}
buttons = {}

for i, led_group in enumerate(leds):
    # Cuadrados para representar los LEDs
    led_square = tk.Button(root, width=10, height=5, bg='red',
                           command=lambda group=led_group: toggle_led(group))
    led_square.grid(row=0, column=i, padx=10, pady=10)
    led_squares[led_group] = led_square
    
    # Cuadrados para representar los push buttons
    button_square = tk.Button(root, width=5, height=3, bg='white',
                              command=lambda group=led_group: toggle_button(group))
    button_square.grid(row=1, column=i, padx=10, pady=5)
    button_squares[led_group] = button_square
    
    # Botones para controlar los LEDs desde la interfaz gráfica
    control_button = tk.Button(root, text=led_group, bg='white',
                               command=lambda group=led_group: control_leds(group))
    control_button.grid(row=2, column=i, padx=10, pady=5)
    buttons[led_group] = control_button

# Función para manejar la recepción de datos desde Arduino
def leer_serial():
    while True:
        mensaje = ser.readline().decode().strip()
        if mensaje:
            print(mensaje)  # Imprime el mensaje recibido de Arduino
            # Actualiza el estado de los cuadrados según el mensaje recibido
            led_group = mensaje.split()[2]
            if mensaje.startswith('Grupo Led'):
                if mensaje.endswith('Encendidos'):
                    led_squares[led_group].config(bg='green')
                elif mensaje.endswith('Apagados'):
                    led_squares[led_group].config(bg='red')
            elif mensaje.startswith('Boton'):
                if mensaje.endswith('Presionado'):
                    button_squares[led_group].config(bg='yellow')
                elif mensaje.endswith('NoPresionado'):
                    button_squares[led_group].config(bg='white')


# Inicia un hilo para leer datos del puerto serie sin bloquear la interfaz gráfica
import threading
threading.Thread(target=leer_serial, daemon=True).start()

root.mainloop()

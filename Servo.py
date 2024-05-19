'''
Programa sencillo que mostrará un mensaje dependiendo del estado del motor Servo.
A = Apagado, cuando se presione el push button 2
E = Encendido, cuando se presione el push button 1

Es posible interrumpir el proceso de girar 180° con el botón de apagado, pero al resumir el proceso con el push button 1, 
el motor regresa a su estado inicial (0°)
'''

import serial

ser = serial.Serial('COM6', 9600, timeout=1)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        if line == 'E':
            print("El Micro motor Servo se encuentra encendido")
        elif line == 'A':
            print("El Micro motor Servo se encuentra apagado")


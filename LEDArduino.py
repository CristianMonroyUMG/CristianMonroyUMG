#Cristian Monroy 0901-22-16592

import serial #Biblioteca serial para la comnunicación serial.
import time #Biblioteca time para las pausas en el proceso de encendido y apagado del led.

ser = serial.Serial('COM9', 9800, timeout=1) #Conecta al COM9 a 9800 baudios con tiempo de espera de 1 segundo.
time.sleep(2)

for i in range(10): #Repetirá el encendido y apagado del led 10 veces.

    ser.write(b'A')  #Envía el byte 'A' a través del puerto serial.
    time.sleep(1) #Pausa de 1 segundo.

    ser.write(b'E') #Envía el byte 'E' a través del puerto serial.
    time.sleep(1) #Pausa de 1 segundo.

ser.close() #Cierra la conexión con el serial.
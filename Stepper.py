'''
Programa que recibirá los valores del potenciómetro que ajusta la velocidad del motor Stepper y las imprimirá en la tereminal de
Visual Studio Code como revoluciones por minuto (rpm).
'''

import serial
import time

# Configura la comunicación serial
puerto_serial = serial.Serial('COM6', 9600, timeout=1)  # Ajusta el puerto COM según sea necesario

print("Iniciando lectura del potenciómetro...")

time.sleep(2)  # Espera 2 segundos para asegurar que la conexión serial está establecida

while True:
        # Lee una línea del puerto serial
        if puerto_serial.in_waiting > 0:
            linea_serial = puerto_serial.readline().decode().strip()
            
            # Verifica si la línea tiene datos válidos
            if linea_serial:
                # Imprime el valor del potenciómetro
                print(f"Velocidad del motor Stepper: {linea_serial} RPM")
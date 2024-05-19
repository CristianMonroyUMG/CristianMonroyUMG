#include <Stepper.h>

// Define los pasos por revolución y los pines de control del motor
const int pasosPorRevolucion = 200;  // Este valor depende del motor
const int pinMotor1 = 8;
const int pinMotor2 = 9;
const int pinMotor3 = 10;
const int pinMotor4 = 11;

// Crea una instancia del objeto Stepper
Stepper miMotor(pasosPorRevolucion, pinMotor1, pinMotor2, pinMotor3, pinMotor4);

// Define el pin del potenciómetro
const int pinPotenciometro = A0;

void setup() {
  // Inicializa la comunicación serie a 9600 baudios
  Serial.begin(9600);
  // Configura el pin del potenciómetro como entrada
  pinMode(pinPotenciometro, INPUT);
}

void loop() {
  // Lee el valor del potenciómetro (0-1023)
  int valorPotenciometro = analogRead(pinPotenciometro);

  // Convierte el valor del potenciómetro a un rango de velocidad (0-60 RPM)
  int velocidad = map(valorPotenciometro, 0, 1023, 0, 60);

  // Establece la velocidad del motor (en RPM)
  miMotor.setSpeed(velocidad);

  // Envia el valor del potenciometro a Python
  Serial.println(velocidad);

  // Gira el motor en una dirección
  miMotor.step(pasosPorRevolucion / 100);  // Gira una fracción de revolución

  // Pausa para evitar lecturas demasiado rápidas
  delay(100);
}

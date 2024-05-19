
//Cristian Monroy 0901-22-16592

#include <Servo.h>

Servo miServo; // Objeto de tipo Servo
const int botonEncendidoPin = 5; // Pin al que está conectado el botón de encendido
const int botonApagadoPin = 4; // Pin al que está conectado el botón de apagado
bool motorEncendido = false; // Estado inicial del motor servo
bool lastEncendidoButtonState = HIGH; // Estado anterior del botón de encendido
bool lastApagadoButtonState = HIGH; // Estado anterior del botón de apagado

void setup() {
  pinMode(botonEncendidoPin, INPUT_PULLUP); // Configura el pin del botón de encendido como entrada con resistencia pull-up
  pinMode(botonApagadoPin, INPUT_PULLUP); // Configura el pin del botón de apagado como entrada con resistencia pull-up
  Serial.begin(9600); // Inicializa la comunicación serial
  miServo.attach(7); // Adjunta el servo al pin 9
}

void loop() {
  bool botonEncendidoState = digitalRead(botonEncendidoPin); // Lee el estado actual del botón de encendido
  bool botonApagadoState = digitalRead(botonApagadoPin); // Lee el estado actual del botón de apagado

  // Detecta el cambio de estado del botón de encendido
  if (botonEncendidoState == LOW && lastEncendidoButtonState == HIGH) {
    motorEncendido = true; // Enciende el motor
    Serial.println('E'); // Enviar 'E' cuando el motor se enciende
    delay(50); // Pequeño retardo para evitar rebotes
  }
  lastEncendidoButtonState = botonEncendidoState; // Actualiza el estado anterior del botón de encendido
  
  // Detecta el cambio de estado del botón de apagado
  if (botonApagadoState == LOW && lastApagadoButtonState == HIGH) {
    motorEncendido = false; // Apaga el motor
    Serial.println('A'); // Enviar 'A' cuando el motor se apaga
    delay(50); // Pequeño retardo para evitar rebotes
    // Espera hasta que se suelte el botón de apagado para evitar el envío múltiple de 'A'
    while (digitalRead(botonApagadoPin) == LOW) {} // Espera hasta que se suelte el botón
  }
  lastApagadoButtonState = botonApagadoState; // Actualiza el estado anterior del botón de apagado

  // Mueve el servo solo si el motor está encendido
  if (motorEncendido) {
    int posicionInicial = 0; // Posición inicial en grados
    int posicionFinal = 180; // Posición final en grados 
    int paso = 40; 

    // Mueve el servo gradualmente de la posición inicial a la final y viceversa
    for (int angulo = posicionInicial; angulo <= posicionFinal; angulo += paso) {
      if (!motorEncendido) break; // Si el motor se apaga, sale del bucle
      miServo.write(angulo); // Establece el ángulo del servo
      delay(500); // Espera 0.5 segundos
      // Verifica el estado del botón de apagado en cada paso
      if (digitalRead(botonApagadoPin) == LOW) {
        motorEncendido = false;
        Serial.println('A');
        // Espera hasta que se suelte el botón de apagado para evitar el envío múltiple de 'A'
        while (digitalRead(botonApagadoPin) == LOW) {} // Espera hasta que se suelte el botón
        break;
      }
    }
    for (int angulo = posicionFinal; angulo >= posicionInicial; angulo -= paso) {
      if (!motorEncendido) break; // Si el motor se apaga, sale del bucle
      miServo.write(angulo); // Establece el ángulo del servo
      delay(500); // Espera 0.5 segundos
      // Verifica el estado del botón de apagado en cada paso
      if (digitalRead(botonApagadoPin) == LOW) {
        motorEncendido = false;
        Serial.println('A');
        // Espera hasta que se suelte el botón de apagado para evitar el envío múltiple de 'A'
        while (digitalRead(botonApagadoPin) == LOW) {} // Espera hasta que se suelte el botón
        break;
      }
    }
  }
}

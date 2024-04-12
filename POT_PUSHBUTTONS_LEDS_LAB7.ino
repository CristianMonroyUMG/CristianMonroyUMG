#include <Arduino.h>

// Definir los pines de los LEDs y los botones
const int ledRaiz = 5;
const int ledRamaIzq = 6;
const int ledRamaDer = 7;
const int ledSubRamaIzq = 8;
const int ledSubRamaDer = 9;
const int pb1 = 2;
const int pb2 = 3;
const int pb3 = 4;
const int potPin = A3;

// Variables para almacenar el estado de los botones y el potenciómetro
int estadoAnteriorPB1 = HIGH;
int estadoAnteriorPB2 = HIGH;
int estadoAnteriorPB3 = HIGH;
int valorPotenciometro = 0;

// Enum para los diferentes estados
enum Estado { PREORDEN, INORDEN, POSTORDEN };
Estado estadoActual = PREORDEN;

void setup() {
  // Inicializar los pines de los LEDs y los botones
  pinMode(ledRaiz, OUTPUT);
  pinMode(ledRamaIzq, OUTPUT);
  pinMode(ledRamaDer, OUTPUT);
  pinMode(ledSubRamaIzq, OUTPUT);
  pinMode(ledSubRamaDer, OUTPUT);
  pinMode(pb1, INPUT_PULLUP);
  pinMode(pb2, INPUT_PULLUP);
  pinMode(pb3, INPUT_PULLUP);

  // Iniciar comunicación serie
  Serial.begin(9600);
}

void loop() {
  // Leer el estado del potenciómetro
  int nuevoValorPotenciometro = analogRead(potPin) / 4; // Escalar el valor a 0-255
  // Enviar el valor del potenciómetro solo si ha cambiado significativamente
  if (abs(nuevoValorPotenciometro - valorPotenciometro) > 5) {
    valorPotenciometro = nuevoValorPotenciometro;
    Serial.print("P");
    Serial.println(valorPotenciometro);
  }

  // Leer el estado de los botones y enviar parámetros si se presionan
  leerBotones();
}

void leerBotones() {
  int estadoPB1 = digitalRead(pb1);
  int estadoPB2 = digitalRead(pb2);
  int estadoPB3 = digitalRead(pb3);

  if (estadoPB1 != estadoAnteriorPB1) {
    if (estadoPB1 == LOW) {
      Serial.println("A");
      digitalWrite(ledRaiz, HIGH);
      delay(1000);
      digitalWrite(ledRamaIzq, HIGH);
      delay(1000);
      digitalWrite(ledSubRamaIzq, HIGH);
      delay(1000);
      digitalWrite(ledSubRamaDer, HIGH);
      delay(1000);
      digitalWrite(ledRamaDer, HIGH);
      delay(1000);
      ApagarLeds();
      estadoActual = PREORDEN;
    }
    estadoAnteriorPB1 = estadoPB1;
  }
  if (estadoPB2 != estadoAnteriorPB2) {
    if (estadoPB2 == LOW) {
      Serial.println("B");
      digitalWrite(ledSubRamaIzq, HIGH);
      delay(1000);
      digitalWrite(ledRamaIzq, HIGH);
      delay(1000);
      digitalWrite(ledSubRamaDer, HIGH);
      delay(1000);
      digitalWrite(ledRaiz, HIGH);
      delay(1000);
      digitalWrite(ledRamaDer, HIGH);
      delay(1000);
      ApagarLeds();
      estadoActual = INORDEN;
    }
    estadoAnteriorPB2 = estadoPB2;
  }
  if (estadoPB3 != estadoAnteriorPB3) {
    if (estadoPB3 == LOW) {
      Serial.println("C");
      digitalWrite(ledSubRamaIzq, HIGH);
      delay(1000);
      digitalWrite(ledSubRamaDer, HIGH);
      delay(1000);
      digitalWrite(ledRamaIzq, HIGH);
      delay(1000);
      digitalWrite(ledRamaDer, HIGH);
      delay(1000);
      digitalWrite(ledRaiz, HIGH);
      delay(1000);
      ApagarLeds();
      estadoActual = POSTORDEN;
    }
    estadoAnteriorPB3 = estadoPB3;
  }
}

// Función para apagar todos los LEDs
void ApagarLeds() {
  digitalWrite(ledRaiz, LOW);
  digitalWrite(ledRamaIzq, LOW);
  digitalWrite(ledRamaDer, LOW);
  digitalWrite(ledSubRamaIzq, LOW);
  digitalWrite(ledSubRamaDer, LOW);
}


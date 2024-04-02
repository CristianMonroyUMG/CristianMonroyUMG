//Cristian Monroy 

// Define variables para mantener el estado de los botones
int estadoBotonA = HIGH;
int estadoBotonB = HIGH;
int estadoBotonC = HIGH;
int estadoBotonD = HIGH;

void setup() {
  pinMode(2, OUTPUT);  // LED 1
  pinMode(3, OUTPUT);  // LED 2
  pinMode(4, OUTPUT);  // LED 3
  pinMode(5, OUTPUT);  // LED 4
  pinMode(6, OUTPUT);  // LED 5
  pinMode(7, OUTPUT);  // LED 6
  pinMode(8, OUTPUT);  // LED 7
  pinMode(9, OUTPUT);  // LED 8

  pinMode(10, INPUT_PULLUP);  // Botón para el grupo A
  pinMode(11, INPUT_PULLUP);  // Botón para el grupo B
  pinMode(12, INPUT_PULLUP);  // Botón para el grupo C
  pinMode(13, INPUT_PULLUP);  // Botón para el grupo D
  
  Serial.begin(9600);
}

void loop() {
  // Leer estado de los botones
  int nuevoEstadoBotonA = digitalRead(10);
  int nuevoEstadoBotonB = digitalRead(11);
  int nuevoEstadoBotonC = digitalRead(12);
  int nuevoEstadoBotonD = digitalRead(13);
  
  // Verificar si el estado de los botones ha cambiado
  if (nuevoEstadoBotonA != estadoBotonA) {
    if (nuevoEstadoBotonA == LOW) {
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      Serial.println("Grupo Led A Encendidos");
    } else {
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      Serial.println("Grupo Led A Apagados");
    }
    estadoBotonA = nuevoEstadoBotonA;
    delay(100); 
  }

  if (nuevoEstadoBotonB != estadoBotonB) {
    if (nuevoEstadoBotonB == LOW) {
      digitalWrite(4, HIGH);
      digitalWrite(5, HIGH);
      Serial.println("Grupo Led B Encendidos");
    } else {
      digitalWrite(4, LOW);
      digitalWrite(5, LOW);
      Serial.println("Grupo Led B Apagados");
    }
    estadoBotonB = nuevoEstadoBotonB;
    delay(100); 
  }

  if (nuevoEstadoBotonC != estadoBotonC) {
    if (nuevoEstadoBotonC == LOW) {
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      Serial.println("Grupo Led C Encendidos");
    } else {
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      Serial.println("Grupo Led C Apagados");
    }
    estadoBotonC = nuevoEstadoBotonC;
    delay(100); 
  }

  if (nuevoEstadoBotonD != estadoBotonD) {
    if (nuevoEstadoBotonD == LOW) {
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
      Serial.println("Grupo Led D Encendidos");
    } else {
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      Serial.println("Grupo Led D Apagados");
    }
    estadoBotonD = nuevoEstadoBotonD;
    delay(100); 
  }
  
  // Control de LEDs a través del puerto serie
  if (Serial.available() > 0) {
    char comando = Serial.read();
    switch (comando) {
      case 'A':
        digitalWrite(2, HIGH);
        digitalWrite(3, HIGH);
        Serial.println("Grupo Led A Encendidos");
        break;
      case 'B':
        digitalWrite(4, HIGH);
        digitalWrite(5, HIGH);
        Serial.println("Grupo Led B Encendidos");
        break;
      case 'C':
        digitalWrite(6, HIGH);
        digitalWrite(7, HIGH);
        Serial.println("Grupo Led C Encendidos");
        break;
      case 'D':
        digitalWrite(8, HIGH);
        digitalWrite(9, HIGH);
        Serial.println("Grupo Led D Encendidos");
        break;
      case 'a':
        digitalWrite(2, LOW);
        digitalWrite(3, LOW);
        Serial.println("Grupo Led A Apagados");
        break;
      case 'b':
        digitalWrite(4, LOW);
        digitalWrite(5, LOW);
        Serial.println("Grupo Led B Apagados");
        break;
      case 'c':
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
        Serial.println("Grupo Led C Apagados");
        break;
      case 'd':
        digitalWrite(8, LOW);
        digitalWrite(9, LOW);
        Serial.println("Grupo Led D Apagados");
        break;
      default:
        // Comando no reconocido
        break;
    }
  }
}


int relayPin = 3;
int loopDelay = 1000;

void setup() {
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH);

  Serial.begin(9600);
  Serial.println("Cristian Monroy");
  delay(2000);
}

void loop() {
  digitalWrite(relayPin, LOW);
  Serial.println("Relay encendido");
  delay(2000);

  digitalWrite(relayPin, HIGH);
  Serial.println("Relay apagado");
  delay(2000);

  Serial.println("======================");

  delay(loopDelay);
}

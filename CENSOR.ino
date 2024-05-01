const int pinSensorTemperatura = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int valorSensor = analogRead(pinSensorTemperatura);

  // Conversión del valor del sensor a temperatura en grados Celsius
  float temperaturaCelsius = (valorSensor / 1023.0) * 5000 / 10;

  // Convertir temperatura a Fahrenheit
  float temperaturaFahrenheit = (temperaturaCelsius * 9 / 5) + 32;

  // Mostrar la temperatura en Celsius y Fahrenheit en el monitor serial
  Serial.print("Temperatura: ");
  Serial.print(temperaturaCelsius);
  Serial.print(" °C / ");
  Serial.print(temperaturaFahrenheit);
  Serial.println(" °F");

  // Esperar un breve periodo de tiempo antes de volver a leer el sensor
  delay(1000);
}


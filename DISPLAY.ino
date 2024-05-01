// Definición de pines para el display de 7 segmentos
const int segmentos[10][7] = {
  {1, 1, 1, 1, 1, 1, 0}, // 0
  {0, 1, 1, 0, 0, 0, 0}, // 1
  {1, 1, 0, 1, 1, 0, 1}, // 2
  {1, 1, 1, 1, 0, 0, 1}, // 3
  {0, 1, 1, 0, 0, 1, 1}, // 4
  {1, 0, 1, 1, 0, 1, 1}, // 5
  {1, 0, 1, 1, 1, 1, 1}, // 6
  {1, 1, 1, 0, 0, 0, 0}, // 7
  {1, 1, 1, 1, 1, 1, 1}, // 8
  {1, 1, 1, 1, 0, 1, 1}  // 9
};

// Definición de pines para el display de 7 segmentos
const int pinesSegmentos[7] = {2, 3, 4, 5, 6, 7, 8};

// Función para mostrar un dígito en el display de 7 segmentos
void mostrarDigito(int numero) {
  for (int i = 0; i < 7; i++) {
    digitalWrite(pinesSegmentos[i], segmentos[numero][i]);
  }
}

void setup() {
  // Configuración de pines
  for (int i = 0; i < 7; i++) {
    pinMode(pinesSegmentos[i], OUTPUT);
  }
}

void loop() {
  // Mostrar el conteo del 0 al 9 en el display de 7 segmentos
  for (int i = 0; i < 10; i++) {
    mostrarDigito(i);
    delay(1000); // Delay de 1 segundo
  }
}

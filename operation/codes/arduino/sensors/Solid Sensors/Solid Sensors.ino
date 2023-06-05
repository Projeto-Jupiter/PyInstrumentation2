#include "HX711.h"

#define DT1 A1
#define SCK1 A0
#define DT2 A2
#define SCK2 A4
#define transducerPin A3

#define SCALE1 436
#define TARE1 50
#define SCALE2 436
#define TARE2 50

#define BAUDRATE 115200

HX711 escala1; // Relaciona a variável da 1a célula de carga
HX711 escala2; // Relaciona a variável da 2a célula de carga

void setup()
{
  Serial.begin(BAUDRATE);
  escala1.begin(DT1, SCK1);
  escala2.begin(DT2, SCK2);

  escala1.set_scale(SCALE1); // Utiliza uma escala padrão de verificação
  escala1.tare(TARE1);       // Fixa o peso como tara
  escala2.set_scale(SCALE2);
  escala2.tare(TARE2);
}

void loop()
{
  int pressureBits = analogRead(transducerPin);
  float pressureBar = (0.309 * pressureBits - 45.3) * 1.03437368199072;

  // Sugestão de implementação da saída: TIMESTAMP, ESCALA1, ESCALA2, PRESSÃO
  Serial.println(
      (String)millis() + "," + (String)escala1.get_units() + "," + (String)escala2.get_units() + "," + (String)pressureBar);
}
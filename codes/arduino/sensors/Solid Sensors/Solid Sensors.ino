#include "HX711.h"

#define DT A1
#define SCK A0
#define transducerPin A3


HX711 escala; // Relaciona a variável escala

void setup() {
 escala.begin (DT, SCK);
 Serial.begin(9600);

 escala.set_scale(436); // Utiliza uma escala padrão de verificação
 escala.tare(); // Fixa o peso como tara
}

void loop() {
  int pressureBits = analogRead(transducerPin);
  float pressureBar = -73.9 + 0.423*pressureBits -2.75*pow(10,-4)*pow(pressureBits,2)+1.21*pow(10,-7)*pow(pressureBits,3);


  Serial.print(millis());
  Serial.print(",");
  Serial.print(escala.get_units(10)); // Retorna peso descontada a tara
  Serial.print(",");
  Serial.println(pressureBar);


 delay(50);
}
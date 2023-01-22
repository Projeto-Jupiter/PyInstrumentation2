#include "HX711.h"

#define DT A1
#define SCK A0
#define transducerPin A3


HX711 escala; // Relaciona a variável escala

void setup() {
 escala.begin (DT, SCK);
 Serial.begin(57600);

 escala.set_scale(436); // Utiliza uma escala padrão de verificação
 escala.tare(50); // Fixa o peso como tara
}

void loop() {
  int pressureBits = analogRead(transducerPin);
  float pressureBar = (0.309*pressureBits - 45.3)*1.03437368199072;


  Serial.println((String)millis() + "," + (String)escala.get_units() + "," + (String)pressureBar);


 delay(25);
}
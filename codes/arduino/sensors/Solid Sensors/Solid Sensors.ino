#include "HX711.h"
#define DT A1
#define SCK A0

HX711 escala; // Relaciona a variável escala

int transducerPin = A3;

void setup() {
  // put your setup code here, to run once:
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

  escala.begin (DT, SCK);
  Serial.begin(9600);
  escala.set_scale(436); // Utiliza uma escala padrão de verificação

  escala.tare(10); // Fixa o peso como tara
}

void loop() {
  // put your main code here, to run repeatedly:

  // read the input on analog pin 0:
  int transducerValue = analogRead(transducerPin);

  // transform analog read into temperature, using the cailbration table 
  // and function, got from comparing with a calibrated pump
  // data: [p(kgf/cm2), bits; 27, 289; 30, 306; 50, 386; 59, 415; 70, 464]
  float pressure = 0.246*transducerValue - 45.208;  

  // print out the pressure:
  Serial.print(millis());
  Serial.print(",");
  Serial.print(escala.get_units()); // print the loadcell value
  Serial.print(",");
  Serial.println(pressure);

  // delay in between reads for stability
  delay(50);  
}
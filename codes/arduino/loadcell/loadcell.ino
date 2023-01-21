#include "HX711.h"

#define DT A1
#define SCK A0

HX711 escala; // Relaciona a variável escala

void setup() {
 escala.begin (DT, SCK);
 Serial.begin(9600);
 Serial.print("Leitura da Tara: ");
 Serial.println(escala.read()); // Aguada o termino de verificação do peso
 Serial.println("Aguarde!");
 Serial.println("Iniciando ...");
 escala.set_scale(436); // Utiliza uma escala padrão de verificação

 escala.tare(20); // Fixa o peso como tara
 Serial.println("Insira o item para Pesar");
}

void loop() {
 Serial.print("Valor da Leitura: ");
 Serial.println(escala.get_units(10)); // Retorna peso descontada a tara
 delay(100);
}
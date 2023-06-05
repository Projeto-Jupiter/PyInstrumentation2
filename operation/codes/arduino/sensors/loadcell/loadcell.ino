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

#define BAUDRATE 9600

HX711 escala1; // Relaciona a variável da 1a célula de carga
HX711 escala2; // Relaciona a variável da 2a célula de carga

void setup()
{
    Serial.begin(BAUDRATE);
    escala1.begin(DT1, SCK1);
    escala2.begin(DT2, SCK2);

    Serial.print("Leitura da Tara 1: ");
    Serial.println(escala1.read()); // Aguada o termino de verificação do peso
    Serial.print("Leitura da Tara 2: ");
    Serial.println(escala2.read()); // Aguada o termino de verificação do peso
    Serial.println("Aguarde!");
    Serial.println("Iniciando ...");
    escala1.set_scale(SCALE1); // Utiliza uma escala padrão de verificação
    escala2.set_scale(SCALE2); // Utiliza uma escala padrão de verificação

    escala1.tare(TARE1); // Fixa o peso como tara
    escala1.tare(TARE2); // Fixa o peso como tara
    Serial.println("Insira os itens a pesar");
}

void loop()
{
    Serial.println("Leitura 1,\t\t Leitura 2: ");
    Serial.println(escala1.get_units(10) + ",\t\t" + escala2.get_units(10)); // Retorna peso descontada a tara
    delay(100);
}
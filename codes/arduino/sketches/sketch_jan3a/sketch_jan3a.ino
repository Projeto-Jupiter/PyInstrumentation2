//Programa: Comunicacao I2C Arduino e Raspberry Pi
//Autor: Arduino e Cia

#include <Wire.h>
#include <MsgPack.h>

struct CustomClass {
    int i;
    float f;

    MSGPACK_DEFINE(i, f); // -> [i, f, s]
};

char str[15];
int valor;
float a;
float b;
char a1[15];
char b1[15];
int A[] = {10000,20000,30000,40000,50000};
CustomClass c;
int i
float f




void setup()
{
  Serial.begin(9600);
  Wire.begin(0x18);
  Wire.onRequest(requestEvent);

}

void requestEvent()
{
  valor = analogRead(A0);
  Serial.println("Requisicao recebida!");
  MsgPack::Packer packer;
  k=packer.serialize c);
  // -> packer.serialize(i, f, s, arr_size_t(3), c.i, c.f, c.s)
  Serial.println(k);
  Wire.write(k);
}

void loop()
{
  delay(50);
}
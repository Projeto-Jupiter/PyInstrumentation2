<<<<<<< Updated upstream:circuits/Transducer/Transducer.ino
int sensorPin = A0;
=======
int sensorPin = A3;
>>>>>>> Stashed changes:codes/arduino/sensors/Transducer/Transducer.ino

void setup() {
  // put your setup code here, to run once:
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  // read the input on analog pin 0:
  int sensorValue = analogRead(sensorPin);

  // transform analog read into temperature, using the cailbration table 
  // and function, got from comparing with a calibrated pump
  // data: [p(kgf/cm2), bits; 27, 289; 30, 306; 50, 386; 59, 415; 70, 464]
  float pressure = -73.9 + 0.423*sensorValue -2.75*pow(10,-4)*pow(sensorValue,2)+1.21*pow(10,-7)*pow(sensorValue,3);
  // print out the pressure:
  Serial.println(pressure);

  // delay in between reads for stability
<<<<<<< Updated upstream:circuits/Transducer/Transducer.ino
  delay(1000);  
=======
  delay(500);  
>>>>>>> Stashed changes:codes/arduino/sensors/Transducer/Transducer.ino
}
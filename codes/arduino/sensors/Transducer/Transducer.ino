int sensorPin = A5;

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
  float pressure = 0.246*sensorValue - 45.208;  

  // print out the pressure:
  Serial.println(sensorValue);

  // delay in between reads for stability
  delay(100);  
}
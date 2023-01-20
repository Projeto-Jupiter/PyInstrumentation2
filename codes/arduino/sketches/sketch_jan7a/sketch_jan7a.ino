struct Data_array{             // Structure declaration
  unsigned long time;            // Member (int variable)
  float thrust;   // Member (float variable)
  float pressure;
};         // Structure variable

Data_array Data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  // Assign values to members of myStructure
  Data.time = millis();
  Data.thrust = analogRead(A0);
  Data.pressure = 10 + Data.thrust/2;
  Serial.print(Data.time);// Print members of myStructure
  Serial.print(",");
  Serial.print(Data.thrust);
  Serial.print(",");
  Serial.println(Data.pressure);// Print members of myStructure

  delay(50);
}

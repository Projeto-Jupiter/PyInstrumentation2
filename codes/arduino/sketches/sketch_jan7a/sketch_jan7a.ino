struct Data_array{             // Structure declaration
  unsigned long time;            // Member (int variable)
  float temperature;   // Member (float variable)
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
  Data.temperature = analogRead(A0);

  Serial.print(Data.time);// Print members of myStructure
  Serial.print(",");
  Serial.print(Data.temperature);
  Serial.print(",");
  Serial.println(Data.temperature);// Print members of myStructure

  delay(50);
}

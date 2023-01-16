int sensorPin = A0;

float resistance = 10000;

void setup() {
  // put your setup code here, to run once:
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

double linearInterpolate(double y, double data[][2])
{
  double x0, x1, y0, y1;
  for (int i = 0; i < sizeof(data) / (sizeof(data[0][0]) * 2); i++)
  {
    if (y > data[i][1] && y < data[i + 1][1])
    {
      y0 = data[i][1];  //lower bound
      y1 = data[i + 1][1]; //upper bound
      x0 = data[i][0];
      x1 = data[i + 1][0];
      return (x0 + ((x1 - x0) * ((y - y0) / (y1 - y0))));
    }
  }
}

double temperature_vs_resistance[][2] = {
  {-30	111.3},
  {-20	67.74},
  {-15	53.39},
  {-10	42.45},
  {-5	33.89},
  {0	27.28},
  {5	22.05},
  {10	17.96},
  {15	14.68},
  {20	12.09},
  {25	10.00},
  {30	8.313},
  {35	6.941},
  {40	5.828},
  {45	4.912},
  {50	4.161},
  {55	3.537},
  {60	3.021},
};

void loop() {
  // put your main code here, to run repeatedly:

  // read the input on analog pin 0:
  int sensorValue = analogRead(sensorPin);

  // remap the output from the range [0,1023] to [0,5]
  // float voltage = map(sensorValue, 0, 1023, 0.0, 5.0); nope, only works for int values
  float voltage = 5.0*sensorValue/1023.0;
  
  //current
  float termistor_resistance = 5.0*resistance/(5.0-voltage) - resistance;

  // print out the value:
  Serial.println(termistor_resistance/1000.0);

  // transform resistance into temperature, using the calibration table
  float temperature = linearInterpolate(resistance, temperature_vs_resistance;

  // print out the value:
  Serial.println(temperature);

  // delay in between reads for stability
  delay(1000);  

}

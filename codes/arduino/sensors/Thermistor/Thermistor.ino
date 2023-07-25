int sensorPin = A0;
float battery_voltage = 3.9;

float resistance = 10.0;

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

{-48,	4.83},
{-46,	4.70},
{-42,	3.77},
{-41,	3.59},
{-40,	3.43},
{-39,	3.27},
{-38,	3.13},
{-37,	3.00},
{-36,	2.87},
{-35,	2.74},
{-34,	2.63},
{-33,	2.51},
{-32,	2.43},
{-31,	2.31},
{-30,	2.24},
{-29,	2.14},
{-28,	2.05},
{-27,	1.98},
{-26,	1.90},
{-25,	1.81},
{-24,	1.75},
{-23,	1.68},
{-22,	1.61},
{-21,	1.56},
{-20,	1.48},
{-19,	1.46},
{-18,	1.40},
{-17,	1.37},
{-16,	1.32},
{-15,	1.25},
{-14,	1.20},
{-13,	1.16},
{-12,	1.11},
{-11,	1.07},
{-10,	1.05},
{-9,	1.01},
{-8,	0.98},
{-7,	0.94},
{-6,	0.92},
{-5,	0.88},
{-4,	0.86},
{-3,	0.83},
{-2,	0.80},
{-1,	0.77},
{0,	0.75},
{1,	0.72},
{2,	0.70},
{3,	0.67},
{4,	0.66},
{5,	0.62},
{6,	0.61},
{7,	0.59},
{8,	0.56},
{9,	0.55},
{10,	0.52},
{11,	0.50},
{12,	0.49},
{13,	0.47},
{14,	0.46},
{15,	0.44},
{16,	0.43},
{17,	0.43},
{18,	0.41},
{19,	0.40},
{20,	0.39},
{21,	0.38},
{22,	0.36},
{23,	0.34},
{24,	0.33},
{25,	0.32},
{26,	0.31},
{27,	0.30},
{28,	0.29},
{29,	0.28},
{30,	0.27},
{31,	0.26},
{32,	0.25},
{33,	0.25},
{36,	0.22},
{37,	0.22},
{38,	0.20},
{40,	0.19},
{43,	0.16},
{50,	0.14},
{52,	0.13},
{55,	0.12},
{57,	0.11},
{59,	0.10},
{62,	0.09},
{65,	0.08},
  
};

void loop() {
  // put your main code here, to run repeatedly:

  // read the input on analog pin 0:
  int sensorValue = analogRead(sensorPin);

  // remap the output from the range [0,1023] to [0,5]
  // float voltage = map(sensorValue, 0, 1023, 0.0, 5.0); nope, only works for int values
  float voltage = battery_voltage*sensorValue/1023.0;
  
  //current
  float termistor_resistance = battery_voltage*resistance/(battery_voltage-voltage) - resistance;

  // print out the value:
  Serial.print("R: ");
  Serial.print(termistor_resistance);
  Serial.print("ohm ");

  // transform resistance into temperature, using the calibration table
  float temperature = linearInterpolate(resistance, temperature_vs_resistance);

  // print out the value:
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print("ºC ");

  //Serial.println(sensorValue);
  Serial.print("V: ");
  Serial.print(voltage);
  Serial.println("V");

  // delay in between reads for stability
  delay(100);  

}

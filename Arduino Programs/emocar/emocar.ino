/********EMOCAR********/

//Variables
const int rightMotorPin = 9;
const int leftMotorPin = 10;
int mode = 0;


void setup()
{
  //set right motor as output
  pinMode(rightMotorPin, OUTPUT);
  
  //set up the serial port
  Serial.begin(9600);
}

void loop()
{
  mode = Serial.read();
  
  //STOP
  if (mode == 0) {
    analogWrite(rightMotorPin, 0);
    analogWrite(leftMotorPin, 0);
  }
  
  //FORWARD
  if (mode == 1) {
    analogWrite(rightMotorPin, 100);
    analogWrite(leftMotorPin, 100);
  }
  
  //LEFT
  if (mode == 2) {
    analogWrite(rightMotorPin, 100);
    analogWrite(leftMotorPin, 0);
  }
  
  //RIGHT
  if (mode == 3) {
    analogWrite(rightMotorPin, 0);
    analogWrite(leftMotorPin, 100);
  }

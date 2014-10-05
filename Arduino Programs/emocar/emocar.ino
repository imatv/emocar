/********EMOCAR********/

//Variables
const int DirA = 13;
const int DirB = 12;
const int pwmA = 3;
const int pwmB = 11;
const int BrkA = 9;
const int BrkB = 8;
char mode[3] = {'s', 's', 'x'};
int leftSpeed = 0;
int rightSpeed = 0;


void setup()
{
  //set motor pwm pins as output
  pinMode(pwmA, OUTPUT);
  pinMode(pwmB, OUTPUT);
  
  //turn off brakes
  digitalWrite(BrkA, 0);
  digitalWrite(BrkB, 0);
  
  //set up the serial port
  Serial.begin(9600);
 
}

void loop()
{ 
  if (Serial.available() > 0) {
    //Read in Serial Data. Return 
    mode[0] = Serial.read();
    mode[1] = Serial.read();
    mode[2] = Serial.read();
    
    ///CASES
    //first letter parsed
    if (mode[0] == 'f') {
      leftSpeed = 200;
      rightSpeed = 200;
      digitalWrite(DirA, HIGH);
      digitalWrite(DirB, HIGH);
    }
    else if (mode[0] == 'b') {
      leftSpeed = -250;
      rightSpeed = -250;
    }
    else {
      leftSpeed = 0;
      rightSpeed = 0;
    }
    
    //second and third letter parsed
    if (mode[1] == 'l') {
      if (mode[2] == 'l') {
        leftSpeed -= 150;
        rightSpeed += 150;
      }
      if (mode[2] == 'h') {
        leftSpeed -= 250;
        rightSpeed += 250;
      }
    }
    else if (mode[1] == 'r') {
      if (mode[2] == 'l') {
        leftSpeed += 150;
        rightSpeed -= 150;
      }
      if (mode[2] == 'h') {
        leftSpeed += 250;
        rightSpeed -= 250;
      }
    }
    
    //Justify the speed values
    if (leftSpeed > 255) {
      leftSpeed = 255;
    }
    if (rightSpeed > 255) {
      rightSpeed = 255;
    }
    
    if (leftSpeed < 0) {
      digitalWrite(DirB, LOW);
      leftSpeed *= -1;
    }
    if (rightSpeed < 0) {
      digitalWrite(DirA, LOW);
      rightSpeed *= -1;
    }
  }
  //Actually write the pins
  analogWrite(pwmA, rightSpeed);
  analogWrite(pwmB, leftSpeed);
  delay(40);
}

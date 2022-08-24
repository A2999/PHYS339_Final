#include <Adafruit_MotorShield.h>
#include <Wire.h>



#define ADDRESS 0x62
float rpm = 50;


Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 1);

const int DistanceToMove = 20; // Input Distance in mm

const int MotorSpeed = 500;  // Motor Speed (Absolute Max 1000)


void setup() {
  // put your setup code here, to run once:
  //Serial.begin(115200);
  AFMS.begin();
  Serial.begin(115200);
  myMotor->setSpeed(255);
}

void loop() {

  
  //if (Serial.available() > 0) {

    myMotor->step(200, FORWARD, DOUBLE);
    //delayMicroseconds(1);
    
    Serial.println(rpm);
    delay(100);



    //myMotor->setSpeed(rpm*2);

    //myMotor->step(200, FORWARD, SINGLE);



  
}

#define DIR_PIN 5
#define PULSE_PIN 6

bool dircurstate = 1;
bool dir = 1;
bool pulse = 0;
int steplimit = 600;
int stepcount = 0;
double turns_sec = 5;

void step(bool dir_, bool pulse_){
  if (dir_ != dircurstate){
    digitalWrite(DIR_PIN, dir);
    delayMicroseconds(5);
    dircurstate = dir_;
  }

  if (pulse_){
    digitalWrite(PULSE_PIN, HIGH);
    delayMicroseconds(3);
    digitalWrite(PULSE_PIN, LOW);
    delayMicroseconds(3);
    delayMicroseconds(int(2500.0/turns_sec));
  }}

void setup() {
  pinMode(DIR_PIN, OUTPUT);
  pinMode(PULSE_PIN, OUTPUT);
  for (stepcount =0; stepcount<steplimit; stepcount++)
    
  {step(1,1);
  }
  delay(300);
  for (stepcount =0; stepcount<steplimit; stepcount++)
    
  {step(0,1);
  }
}






void loop() {
  // put your main code here, to run repeatedly:
//  step(dir, 1);
//  
//  if(stepcount < steplimit){
//    stepcount++;
//  }
//  else{
//    stepcount = 0;
//    dir = !dir;
  }

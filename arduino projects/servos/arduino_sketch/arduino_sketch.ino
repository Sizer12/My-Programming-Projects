#include <Servo.h>
Servo servo1 ;
Servo servo2 ;
Servo servo3 ;
Servo servo4 ;
int pot1 = A0;
int pot2 = A1;
int pot3 = A2;
int pot4 = A3;
int val1;
int val2;
int val3;
int val4;

void setup(){
  servo1.attach(9);
  servo2.attach(10);
  servo3.attach(11);
  servo4.attach(13);
  }
void loop(){
  val1 = analogRead(pot1);
  val1 = map(val1,0,1023,0,180);
  servo1.write(val1);
  val2 = analogRead(pot2);
  val2 = map(val2,0,1023,0,180);
  servo2.write(val2);
  val3 = analogRead(pot3);
  val3 = map(val3,0,1023,0,180);
  servo3.write(val3);
  val4 = analogRead(pot4);
  val4 = map(val4,0,1023,0,180);
  servo4.write(val4);
  
  
  
  }

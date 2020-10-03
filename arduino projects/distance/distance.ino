#include <LiquidCrystal.h>

LiquidCrystal lcd(1, 2, 4, 5, 6, 7); 

const int trigPin = 9;
const int echoPin = 10;
int redled = 11;
int yellowled = 12;
int greenled = 8;
long duration;
int distanceCm, distanceInch;

void setup() {
Serial.begin(9600);
lcd.begin(16,2); 
pinMode(redled,OUTPUT);
pinMode(yellowled,OUTPUT);
pinMode(greenled,OUTPUT);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
}

void loop() {
digitalWrite(trigPin, LOW);
delayMicroseconds(2);

digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

duration = pulseIn(echoPin, HIGH);
distanceCm= duration*0.034/2;
distanceInch = duration*0.0133/2;

lcd.setCursor(0,0); 
lcd.print("Distance: "); 
lcd.print(distanceCm);
lcd.print(" cm");
delay(10);
lcd.setCursor(0,1);
lcd.print("Distance: ");
lcd.print(distanceInch);
lcd.print(" inch");
delay(100);

if(distanceCm > 10){
  digitalWrite(redled,LOW);
  }
else{
  digitalWrite(redled,HIGH);
  
  }
if(distanceCm > 15){
  digitalWrite(yellowled,LOW);
  }
else{
  digitalWrite(yellowled,HIGH);
  
  }
if(distanceCm > 20){
  digitalWrite(greenled,LOW);
  }
else{
  digitalWrite(greenled,HIGH);
  }


  }

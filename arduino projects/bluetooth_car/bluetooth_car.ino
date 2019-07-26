#include <Servo.h>
#include <SoftwareSerial.h>
SoftwareSerial hc06(6,7);
String cmd="";
int redLed =5;
int greenLed =4;
Servo myservo;
int speed = 1;

void setup(){
  Serial.begin(9600);
  hc06.begin(9600);  
  myservo.attach(9);
  myservo.write(0);
  pinMode(redLed,OUTPUT);
  pinMode(greenLed,OUTPUT);
  digitalWrite(redLed,HIGH);
  digitalWrite(greenLed,HIGH);
}
void loop(){
  while(hc06.available()>0){
    cmd+=(char)hc06.read();
  }
 
  if(cmd!=""){
    if(cmd == "HIZLAN"){
      if(!(speed == 0)){}
      speed--;
      }
    else if(cmd == "YAVASLA"){
      speed++;
      }
    else if(cmd == "AC"){
      digitalWrite(redLed,HIGH);
      digitalWrite(greenLed,LOW);      
      for(int pos = 0; pos <= 90; pos++){
        myservo.write(pos);
        delay(speed);
        }
      Serial.println("Açıldı");
      }
    else if(cmd == "KAPA"){
      digitalWrite(redLed,LOW);
      digitalWrite(greenLed,HIGH);
      for(int pos = 90; pos >= 0; pos--){
        myservo.write(pos);
        delay(speed);
        }
      Serial.println("Kapandı");
      }
  }
    cmd="";
    delay(100);
 }

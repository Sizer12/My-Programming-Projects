#include <SoftwareSerial.h>
#include <LiquidCrystal.h>

SoftwareSerial hc06(6,7);
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

String cmd="";
int resetPin = 8;

void setup(){
  pinMode(resetPin,OUTPUT);
  lcd.begin(16, 2);
  Serial.begin(9600);
  hc06.begin(9600);
}
void loop(){
  while(hc06.available()>0){
    cmd+=(char)hc06.read();
  }
 
  if(cmd!=""){
    if(cmd == "clear"){
       lcd.clear();
      }
    else{
      Serial.println(cmd);
            
      String s1 = cmd.substring(0,15);
      String s2 = cmd.substring(15,31);
      
      lcd.setCursor(0,0);
      lcd.print(s1);
      lcd.setCursor(0,1);
      lcd.print(s2);
      }
  }
    cmd="";
    delay(100);
 }

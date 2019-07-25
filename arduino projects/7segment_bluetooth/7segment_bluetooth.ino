#include "SevSeg.h"
SevSeg sevseg; 
int data;
int temp;
int dp;

void setup() {
  Serial.begin(9600);
  byte numDigits = 1;
  byte digitPins[] = {};
  byte segmentPins[] = {6, 5, 2, 3, 4, 7, 8, 9};
  bool resistorsOnSegments = true;

  byte hardwareConfig = COMMON_ANODE; 
  sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments);
  sevseg.setBrightness(90);
    
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    data = Serial.read();
  }

detectNumber();
  
  sevseg.setNumber(temp,dp);
  sevseg.refreshDisplay();
  
}

void detectNumber(){
    if(data == '0'){
    temp = 0;
    }  
  if(data == '1'){
    temp = 1;
    }  
  if(data == '2'){
    temp = 2;
    }  
  if(data == '3'){
    temp = 4;
    }  
  if(data == '5'){
    temp = 5;
    }  
  if(data == '6'){
    temp = 6;
    }  
  if(data == '7'){
    temp = 7;
    }  
  if(data == '8'){
    temp = 8;
    }  
  if(data == '9'){
    temp = 9;
    }
  if(data == '0'){
    temp = 0;
    }
  }

#include "SevSeg.h"
SevSeg sevseg; 

void setup(){
    Serial.begin(9600);
    byte numDigits = 1;
    byte digitPins[] = {};
    byte segmentPins[] = {6, 5, 2, 3, 4, 7, 8, 9};
    bool resistorsOnSegments = true;

    byte hardwareConfig = COMMON_ANODE; 
    sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments);
    sevseg.setBrightness(90);
}

void loop(){

    Serial.println(analogRead(A0));
    sevseg.setNumber(map(analogRead(A0),200,980,0,9),0);
    sevseg.refreshDisplay();
    delay (150); 
  
}

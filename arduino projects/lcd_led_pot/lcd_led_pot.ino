#include <LiquidCrystal.h>

/*
Author: Danny van den Brande, Arduinosensors.nl. BlueCore Tech.
NOTE:There is a difference in RGB Leds, Common Annode and Common Cathode
Add common anode to 5v and Common Cathode to GND.
The longest pin on the RGB Led is the Cathode or Annode pin.
If it does not work on 5v it is a Annode.
If it does not work on GND it is a Cathode.
 */

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int redPin = 9; //Pin for the red RGB led pin
int greenPin = 10; //Pin for the green RGB led pin
int bluePin = 11; //Pin for the blue RGB led pin
 
int potPin_red = A2;  //declare pin for the potentiometer for the red LED
int potPin_green = A1;  //declare pin for the potentiometer for the green LED
int potPin_blue = A0;  //declare pin for the potentiometer for the blue LED
 
int readValue_red; //declare variable to store the read value from the potentiometer which controls the red LED
int readValue_green; //declare variable to store the read value from the potentiometer which controls the green LED
int readValue_blue; //declare variable to store the read value from the potentiometer which controls the blue LED
 
int writeValue_red; //declare variable to send to the red LED
int writeValue_green; //declare variable to send to the green LED
int writeValue_blue; //declare variable to send to the blue LED
 
void setup() {
  lcd.begin(16,2);
  pinMode(potPin_red, INPUT); //set potentiometer for red LED as input
  pinMode(potPin_green, INPUT); //set potentiometer for green LED as input
  pinMode(potPin_blue, INPUT); //set potentiometer for blue LED as input
  
  pinMode(redPin,OUTPUT); //set pin for red LED as output
  pinMode(bluePin,OUTPUT); //set pin for green LED as output
  pinMode(greenPin, OUTPUT); //set pin for blue LED as output
}
 
void loop() {
  lcd.setCursor(0, 0);
  lcd.print("R:");
  lcd.setCursor(2, 0);
  lcd.print(writeValue_blue);
  lcd.setCursor(5, 1);
  lcd.print("G:");
  lcd.setCursor(7,1);
  lcd.print(writeValue_green);
  lcd.setCursor(10, 0);
  lcd.print("B:");
  lcd.setCursor(12,0);
  lcd.print(writeValue_red);

  
  readValue_red = analogRead(potPin_red); //Read voltage from potentiometer to control red LED
  readValue_green = analogRead(potPin_green); //Read voltage from potentiometer to control green LED
  readValue_blue = analogRead(potPin_blue); //Read voltage from potentiometer to control blue LED
  
  writeValue_red = (255./1023.)*readValue_red; //Calculate the value to write on the red LED (add point to change to float point)
  writeValue_green = (255./1023.)*readValue_green; //Calculate the value to write on the green LED
  writeValue_blue = (255./1023.)*readValue_blue; ///Calculate the value to write on the blue LED
  
  analogWrite(redPin,writeValue_red); //write value to set the brightness of the red LED
  analogWrite(greenPin,writeValue_green); //write value to set the brightness of the green LED
  analogWrite(bluePin,writeValue_blue); //write value to set the brightness of the blue LED
}

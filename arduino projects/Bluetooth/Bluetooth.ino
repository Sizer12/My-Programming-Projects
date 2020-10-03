int redLed = 13;
int greenLed = 12;
int yellowLed = 11;
int data;

void setup() {
  // put your setup code here, to run once:
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(yellowLed, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  while (Serial.available() > 0) {     //wait here until the data is available
    data = Serial.read();
  }

  if (data == '1') {
    digitalWrite(redLed, HIGH);
    digitalWrite(greenLed, LOW);
    digitalWrite(yellowLed, LOW);
    Serial.println("Red On");
    data = '4';
  }

  if (data == '2') {
    digitalWrite(redLed, LOW);
    digitalWrite(greenLed, HIGH);
    digitalWrite(yellowLed, LOW);
    Serial.println("Green On");
    data = '4';
  }

  if (data == '3') {
    digitalWrite(redLed, LOW);
    digitalWrite(greenLed, LOW);
    digitalWrite(yellowLed, HIGH);
    Serial.println("Yellow On");
    data = '4';
  }

  // put your main code here, to run repeatedly:

}

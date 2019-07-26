const int leftForward = 2;
const int leftBackward = 3;
const int rightForward = 4;
const int rightBackward = 5;
void setup() {
  // put your setup code here, to run once:
  pinMode(leftForward,OUTPUT);
  pinMode(leftBackward,OUTPUT);
  pinMode(rightForward,OUTPUT);
  pinMode(rightBackward,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(leftForward,HIGH);
  digitalWrite(leftBackward,LOW);
  digitalWrite(rightForward,HIGH);
  digitalWrite(rightBackward,LOW);
}

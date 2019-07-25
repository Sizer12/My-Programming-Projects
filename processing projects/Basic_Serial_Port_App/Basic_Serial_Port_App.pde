import processing.serial.*;

Serial myPort;

void setup()
{
  myPort = new Serial(this, Serial.list()[4], 9600);
  println(Serial.list());
}


void draw()
{
}


void keyPressed() {

  switch (key) {

  case 'w':
    myPort.write('1');
    break;

  case 'p':
    myPort.write('2');
    break;

  default:
    myPort.write('0');
  }
}

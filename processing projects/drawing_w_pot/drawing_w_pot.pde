import processing.serial.*;
Serial port;
float brightness = 0;

void setup(){
  size(640,360);
  port = new Serial(this, "COM3", 9600);
  port.bufferUntil('\n');
  
}
void draw(){
  if(mousePressed == true){
    stroke(255,150,240);
    line(pmouseX,pmouseY,mouseX,mouseY);
    
    background(110,19,94);
  }
  
}

void serialEvent (Serial port)
{
  brightness = float(port.readStringUntil('\n'));
}

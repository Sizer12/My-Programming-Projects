int colour = 0;
void setup()
{
  size(500,500);
  background(0);
}
void draw()
{ 
  if(keyPressed ){if(keyCode == UP){colour++;}if(colour>255){colour=255;}}
  if(keyPressed ){if(keyCode == DOWN){colour--;}if(colour<0){colour=0;}}
  if(keyPressed ){if(key == 32){clear();}}
  if(mousePressed){
    stroke(255);
    fill(colour);
    if(mouseButton == LEFT){ellipse(mouseX,mouseY,100,100);}
    else if(mouseButton == RIGHT){rect(mouseX-50,mouseY-50,100,100);}
  }

}

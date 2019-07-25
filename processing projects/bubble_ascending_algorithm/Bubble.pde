class Bubble {

  float x;
  float y;
  int i;
  float diameter;
  
  Bubble(float tempD){
    
    x = width/2;
    y = height;
    diameter = tempD;
    
  }
  
  void ascend(){
    y--;
    x = x+ random(-10,10);
  }
  void display() {
    stroke(0);
    fill(255,150,240);
    ellipse(x,y,diameter,diameter);  
  }
  void top(){
    if(y<diameter/2){
      y=diameter/2;
    }
  }
  


  

  
  







}

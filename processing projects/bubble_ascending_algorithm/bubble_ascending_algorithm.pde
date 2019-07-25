Bubble b1;
Bubble b2;


void setup(){
  size(640,340);
  b1 = new Bubble(10);
  b2 = new Bubble(64);
}

void draw(){
  background(110,19,94);
  b1.display();
  b1.ascend();
  b1.top();
  b2.display();
  b2.ascend();
  b2.top();
  }
  


   

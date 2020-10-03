const int LEDdizisi[] = {2,3,4,5,6,7,8,9,10,11};

void setup() {
  for(int i=0; i<10 ;i++)    
  { 
    pinMode(LEDdizisi[i], OUTPUT);
  }
}

void loop() {
  
  for(int i=0; i<10; i++){ 
    digitalWrite(LEDdizisi[i],LOW);      
    delay(50);                           
    digitalWrite(LEDdizisi[i],HIGH);         
  }
 
  for(int j=9;j>=0; j--)
  { digitalWrite(LEDdizisi[j],LOW);     
    delay(50);
    digitalWrite(LEDdizisi[j], HIGH);
  } 
}

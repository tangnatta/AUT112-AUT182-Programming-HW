// C++ code 
// 
int dec=19;  
String bin; 
void setup() 
{ 
	Serial.begin(9600); 
  	while (num>0){ 
  		bin=dec%2+bin; 
  		dec=dec/2; 
  	}   
  	Serial.print(dec); 
} 

  

void loop() 

{  

} 
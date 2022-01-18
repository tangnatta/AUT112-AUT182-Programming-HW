// C++ code
//Q3 - LAB3
float a= 8,b= 5,c= 8;
float s, area;
void setup()
{
  Serial.begin(9600);
  s=(a+b+c)/2;
  area=sqrt(s*(s-a)*(s-b)*(s-c));
  Serial.println(area);
}

void loop()
{
	
}
// C++ code
//Q1 - LAB3
int AD, BE;
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available()>0){
  	AD = Serial.parseInt();
    BE = AD + 543;
  	Serial.println(BE);
    sumall(AD);
    sumall(BE);
  }
}

void sumall(int num)
{
   	int sum = 0;
    while (num > 0) 
    {
        sum = sum+(num%10);
        num = num/10;
    }
    Serial.println(sum);
}
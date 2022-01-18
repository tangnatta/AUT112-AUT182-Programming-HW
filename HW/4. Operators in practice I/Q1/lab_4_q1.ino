// C++ code
//Q1 - LAB 4
float BMI, weight, height;
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available()>0){
    weight = Serial.parseFloat();
    while (true) {
      if (Serial.available()>0){
         height = Serial.parseFloat();
         BMI = weight/pow(height,2);
         Serial.println(BMI);
         break;
      }
    }
  }
}
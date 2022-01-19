// C++ code
//
int oneortwo,num,time,counter;
float dec;
String bin,numstr,result,numnow;
void setup()
{
  Serial.begin(9600);
}

void loop()
{
	if (Serial.available()>0){
  		oneortwo = Serial.parseInt();
      Serial.println(oneortwo);
      	while (true) {
      		if (Serial.available()>0){
         		num = Serial.parseInt();
              Serial.println(num);
              find_bin_and_dec();
              break;
            }
        }
    }
}

void find_bin_and_dec()
{
  if (oneortwo==1) {
    dectobin();
  }
  else if (oneortwo==2) {
    bintodec();
  }
}

void dectobin()
{
  while (num>0){
  	bin=num%2+bin;
  	num=num/2;
  }  
  Serial.print(bin);
}

void bintodec()
{
  time=sizeof(num);
  numstr=String(num);
  while (time>0){
    numnow=numstr[time-1];
  	dec=dec+((numnow.toInt())*(pow(2,(sizeof(num)+1-time))));
    time=time-1;
  }
  Serial.println(dec);
}
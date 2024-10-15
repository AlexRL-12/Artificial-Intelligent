
#include <Servo.h>

Servo servoBase;//Asigno un nombre específico
int grados = -1;
int option ;

void setup() {
   servoBase.attach(3);//Pin a utilizar para servo
   Serial.begin(9600);
   servoBase.write(0);
}

void loop() {
   
  grados = servoBase.read();

  Serial.println(grados);

  if(grados != 0){
    servoBase.write(0);
  }

  if(Serial.available() > 0){

    option = Serial.read();

      Serial.println(option);

    if(option == '1'){
      
      servoBase.write(180);
      Serial.println("entro");
      delay(15000);
      servoBase.write(0);
      delay(5000);
    }
 
  }
}

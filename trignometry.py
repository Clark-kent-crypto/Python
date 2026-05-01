import math as mt
anG=int(input("What is the angle :"));
class value:
 
#  pi=3.1415;
 anGRad=(mt.pi/180.0)*anG;
 turns=anG/0.001;
 anGsmall=anGRad/turns;
 trigno=[];
def sin(value):
 anGx=1;
 anGy=0;
 for i in range(0,int(value.turns),1):
   anGxNew=anGx-(anGy*value.anGsmall);
   anGyNew=anGy+(anGx*value.anGsmall);
   anGx=anGxNew;
   anGy=anGyNew;
 value.trigno.append(anGxNew);
 value.trigno.append(anGyNew);

sin(value);
print("Which value do you need :");
print("1.Sin");
print("2.Cos");
try:
  run=int(input("Enter the choice :"));
except:
  print("Enter a valid option :")
if(run==1):
 print("Sin value is :",value.trigno[1]);
elif(run==2):
 print("Cos value is :",value.trigno[0]);
# print(value.trigno[0:2]);
 


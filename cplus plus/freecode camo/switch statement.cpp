#include<iostream>
using namespace std;

string day(  int dayNum){

string dayNum1;

switch(dayNum) {

case 0:

  dayNum1 = "sunday";
  break;
case 1:
    dayNum1 = "mounday";
    break;
case3:
    dayNum1 = "Tuesday";
    break;
case4:
  dayNum1 = "wednesday";
  break;
case5:
    dayNum1= "thursday";

    break;
case6:
    dayNum1 = " friday ";
    break;
case 7:
    dayNum1 = "saturday";




    break;
default:
    dayNum1 = "invalid operation";
}

return dayNum1;
}
int main(){

cout<< day(1);
return 0;
}

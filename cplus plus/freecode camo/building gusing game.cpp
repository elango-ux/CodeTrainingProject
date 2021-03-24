#include<iostream>
using namespace std;
int main (){

int secretNumber = 7;
int guesingNo;
int gusscount =0;
int gusslimit = 3;
int outofguss =  false;


while(secretNumber != guesingNo && !outofguss){
      cout<<!outofguss;

    if(gusscount< gusslimit){
    cout <<"guess a number";
cin>> guesingNo;
gusscount++;
}

else {
       outofguss = true;

    break;
}
}
return 0;
}

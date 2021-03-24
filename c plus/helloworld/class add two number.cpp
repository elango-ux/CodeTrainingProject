#include<iostream>
using namespace std;

class Add {
public:
int Num1,Num2;
Add(int num1, int num2){

Num1 = num1;
Num2 = num2;

}

int sum(){

  return Num1 + Num2;

}
};




 int main(){


int num1;
int num2;
cout<<"Enter  a  number1: \n ";
cin>> num1;
cout<<"Enter number2: \n ";
cin>> num2;
Add add1 = Add( num1,num2);
cout<< add1.sum();





 return 0;
 }

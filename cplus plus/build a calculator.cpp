#include<iostream>
using namespace std;
int main(){
int number1;
int number2;
char oper;
cout<< " enter a number 1";
cin>> number1;
cout<< " enter a number 2";
cin>> number2;
cout<< " enter a operator";
cin>> oper;
int result;
if(oper == '+'){

    result = number1 + number2;

}
else if (oper == '-'){
 result = number1 - number2;}
else if (oper == '*'){

    result = number1* number2;
}
else{

    cout<<"invalid operation";
}

cout << result;

return 0;
}

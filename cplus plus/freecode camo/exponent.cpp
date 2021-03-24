#include<iostream>
using namespace std;


int power(int baseNo,int powerNo){
  int result = 1;

 for(int i =0;i < powerNo; i++){
     result = result*baseNo;

 }
return result;
}

int main(){
cout<< power(2, 5);

return 0;
}

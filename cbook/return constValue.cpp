#include<iostream>
using namespace std;


// *fun is pointer to char;
//
const char *fun();

int main(){
   //*p is pointer to char
   const char  *p;
   p = fun();
    *p = 'A';
   cout<<p;
return 0;
}
const char *fun(){

return "rain";
}

#include<iostream>
using namespace std;


char  fun(char *s){

  return  s[5];
}

int main(){

char str[20] =  "wgwefewfewfewdsw";
char ch;
ch = fun(str);
cout<<ch;
return 0;
}

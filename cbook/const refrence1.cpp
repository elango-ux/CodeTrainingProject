
#include<iostream>
using namespace std;
int main(){
const int i =10;
int&j = i;
cout<<i<<endl<<j;
j=20;
cout<<"i="<<i<<"j="<<j;
return 0;
}

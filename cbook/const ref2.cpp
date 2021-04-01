#include<iostream>
using namespace std;
int main(){

int i = 10;
const int &j =i;
cout<<i<<endl<<j;

j= 20;
cout<<i<<j;







return 0;
}

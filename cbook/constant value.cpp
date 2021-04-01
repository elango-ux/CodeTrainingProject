#include<iostream>
using namespace std;




int f3() { return 8; }


const int f4() { return 1; }





int main(){



const int j = f3();
cout<<j<<endl;
int k = f4();
cout<<k<<endl;







return 0;
}

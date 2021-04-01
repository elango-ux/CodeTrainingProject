#include <iostream>
using namespace std;

// Global variable declaration
int c = 12;

void test();
void test1();
int main()
{
    ++c;

    // Outputs 13
    cout << c <<endl;
    test();
    test1();
return 0;
}
void test(){

 ++c;
cout<<c;




}
void test1(){

++c;
cout<<c;



}

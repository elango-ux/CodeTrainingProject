
#include<iostream>
using namespace std;

class AbstractBase
{
 public:
 virtual void Display() = 0; //Pure Virtual Function declaration
};

class Derived:public AbstractBase
{
 public:
 void Display()
 {
	 cout << "pure virtual function implementation"; }
 };
 int main() {

 AbstractBase *basePointer = new Derived(); basePointer->Display();

 // OR
 AbstractBase * bPtr;
 Derived dObj;
 bPtr = &dObj;
 bPtr->Display();

}

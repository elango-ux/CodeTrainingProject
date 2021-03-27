#include<iostream>
using namespace std;

class Base{
public:
virtual void show()=0;
};


class Derived:public Base
{
public:
    void show(){
     cout << "Implementation of Virtual Function in Derived class\n";
}
};
int main()
{
Base *obj;
Derived d;
 obj = &d;
 obj->show();
 return 0;
}

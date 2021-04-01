
#include<iostream>
using namespace std;
struct employee
{

    char name[20];
    int age;
    float salary;

};

void displayVal(employee);
void displayAddr(employee *);
void displayRef(employee &);
int main(){


employee e = {"sanjay",32,32000.00};
employee k {"rahul",32,98000};
displayVal(e);
displayAddr(&e);
displayRef(e);

return 0;
}
void displayVal(employee e){
cout<<e.name;
}
void displayAddr(employee *p){
cout<<p->name;
}
void displayRef(employee &p){


cout<<p.name;


}

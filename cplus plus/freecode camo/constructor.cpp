#include<iostream>
using namespace std;
class Employee {


public:
    string Name;
    string Company ;
    int Age;

  void employeeInformation(){


  cout<< my name is<<Name<< endl;
  cout<<i am working  in <<company<<endl;
  cout<< my  age is<< Age;

}



  Employee(string name, string company, age){

        Name = name;
       Company = company;
       Age = age;
}
};


int  main(){

Employee employ("elango","halnode",28);
employ.employeeInformation();







return 0;
}


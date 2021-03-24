#include<iostream>
using namespace std;
class Employee {

private:
   int salary;
public:
     int setsalary(int sal){

            salary = sal;

     }
     int getsalary(){
        return salary;

     }

};

int main(){
Employee employee1;
 employee1.setsalary(50000);
cout<< employee1.getsalary();
return 0;
}

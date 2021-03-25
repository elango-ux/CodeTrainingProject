#include<iostream>
using namespace std;

class Employee {

private:
    string Name;
    string Company;
    int Age;
public:
void IntroduceYourself(){
cout<<"Name: "<< Name<<endl;
cout<<"Company: "<<Company<<endl;
cout<<"Age: "<<Age;
}
void setName(string nam){

  Name = nam;


}
string getName(){

return Name;
}
void setCompany(string com){

  Company = com;


}
string getCompany()
{

    return Company;

}
void setAge(int ag){
if(ag> 0 && ag <100){
 Age = ag;} else {

  Age =0;

 }
}
int getAge(){

return Age;


}


Employee(string name, string company , int age){

    Name =  name;
    Company = company;
    Age = age;

}


};
int main(){
Employee employee1 =  Employee("Elango ", "halnode", 28);


employee1.IntroduceYourself();
employee1.setName("ravi");

cout<<employee1.getName();
employee1.setCompany("halnode");
cout<< employee1.getCompany();
employee1.setAge(105);
cout<<employee1.getAge();
return 0;

}

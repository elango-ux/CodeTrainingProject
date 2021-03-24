#include<iostream>
using namespace std;


class Person {
private:
    string name;
    int age;
public:
    Person(string n, int a){

           name = n;
           age  = a;

}

void display(){
cout<< name<<age;
}
void setAge(int a) {
  if ((a >= 0) && (a <= 120)) {
    age = a;
  }
  else {
    age = 0;
  }

}
};





int main(){


Person person1 = Person("elango ", 90);
//person1.setAge(1000);
person1.display();
Person person2 = Person("karthick ", 21);
person2.display();

person2.setAge(45);
Person2.display();
return 0;
}

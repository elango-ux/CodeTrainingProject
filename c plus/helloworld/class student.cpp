#include<iostream>
using namespace std;


class Student{
public:
    char *Name;
    int Mark1;
    int Mark2;
Student(name,mark1,mark2){
    Name = name;
    Mark1 = mark1;
    Mark2 = mark2;
}
int cal_media(){
       return Mark1+ Mark2/2;

}
int display(){
cout<<"Name: " << Name;
cout<<"media" <<cal_media();

}





};







int main(){
char *name;
int mark1, mark2;
cout<<"enter the name";
cin>> name;
cout<<"enter the mark1  and mark2\n";
cin >> mark1;
cin>> mark2;

Student stu1 = Student(name, mark1,mark2);
stu1.display();

return 0;
}



#include<iostream>
using namespace std;
int main(){

class Student {

public:





Student(){
cout<<"rrrrrr";
}

string Name;
string Major;
int Gpa;
Student(string aName, string aMajor, int agpa){

Name = aName;
Major = aMajor;
Gpa = agpa;
}







};

Student student1("elango", "art", 2.8);
Student  student2( "karthick", "social", 3.6);


cout<< student1.Name;


return 0;


}

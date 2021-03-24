#include<iostream>
using namespace std;
int main(){

 class Student {
 public:
     string name;
     string major;
     int gpa;
 Student(string aname, string bmajor, int cgpa){
      name = aname;
       major = bmajor;
      gpa = cgpa;
     }

     bool hasHonour(){

     if(gpa> 2.3){
        return true;


     }


        return false;

     }


};

Student student1("elango", "art", 3.9);
student1.major = "science";
cout<< student1.major;
Student student2("ravi", "science", 4.7);
cout<< student1.hasHonour();

return 0;
}

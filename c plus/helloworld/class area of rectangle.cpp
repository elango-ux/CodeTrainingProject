#include<iostream>
using namespace std;
int main(){

class Area {

private:

int Length, Breadth;


Area(int length, int breadth){

  Length = length;
  Breadth = breadth;

}

int areaofRectangle(){


return Length*Breadth;


}



};



int length;
int breadth;
cout<< "enter the length";
cout<< "enter the breadth";
Area   area1 = Area(length, breadth);
cout<< area1.areaofRectangle();


return 0;
}

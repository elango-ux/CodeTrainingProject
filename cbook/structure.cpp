#include<iostream>
using namespace std;


struct Smartphone {

    string name;
    int storagespace;
    string color;
    float price;
};
aawint main(){

//assign value;
Smartphone smartphone;
smartphone.name = " iphone 12";
smartphone.storagespace =32;
smartphone.color = "black";
smartphone.price =  888.99;
Smartphone smartphone2;
smartphone2.name = "samsung galaxy s12 ultra";
smartphone2.storagespace = 32;
smartphone2.color ="black";
smartphone2.price = 999.99;


cout<<"name: " <<smartphone.name<<endl;
cout<<"storageSpace: " <<smartphone.storagespace<<endl;
cout<<"color: "<<smartphone.color<<endl;
cout<<"price: "<<smartphone.price<<endl;


return 0;
}

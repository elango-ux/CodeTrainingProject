#include<iostream>
using namespace std;
int main()
{

   bool isMale = true;
   bool isTall = false;
    if(isMale && isTall){

        cout<< "he is male";}

    else if(!isMale && isTall){

         cout<< "he is short";
}

   else if(isMale && !isTall){

    cout<< "you are tall but not male";

   }

    else {

        cout<< "he is not male";
    }





    return 0;
}

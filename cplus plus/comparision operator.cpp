#include<iostream>
using namespace std;

double getMax(int num1, int num2, int num3) {
int result;
cout<<" result 1 "<< result;
if(num1 >= num2 && num1 >= num3) {

 result = num1;
    cout<< "result 2 " << result;
}
else if (num2 >= num1 && num2>= num3){

    result = num2;
    cout<<"result 3 " << result;

} else {
    result = num3;
    cout <<"result 4 "<< result;
}
cout << result;

return result;
}
int main(){



cout <<" result 5 "<< getMax(4,6,7);




return 0;

}

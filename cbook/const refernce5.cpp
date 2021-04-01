#include<iostream>
using namespace std;
int main()
{

    char *str1 = "rain rain hear again";
    char  *&str2 = str1;
    cout<<endl<<str1<<endl<<str2;

    *str2 ="M";


    return 0;
}

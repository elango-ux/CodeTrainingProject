#include <iostream>
using namespace std;

int main(){

// newline
cout << " giraffe academy\n";
cout << " hello \n\n";
cout << "fly \n";
// storing string in variable
string  name = "elango is a good boy\n";
cout << name;
//length of string using string function

 cout <<name.length() << "\n";

 // to access specific character in the string
  cout << name[2] <<"\n";
//modify character of string
 name[2]= 'A';
cout<< name;
cout << name.find("is", 0)<<"\n";
cout << name.find( "good",0)<<"\n";
cout<< name.find('i',0)<<"\n";
cout<< name.substr(8,3);

return 0;

}

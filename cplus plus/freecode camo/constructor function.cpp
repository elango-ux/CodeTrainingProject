#include<iostream>
using namespace std;
int main(){

class Book {


public:
    string title;
    string author;
    int age;

Book(string atitle, string bauthor, int aage){
          title = atitle;
          author = bauthor;
          age =  aage;

}

};

Book book1(" harrypotter", " jfjffjfjfj ", 25);
book1.title= " jjjjjjjjjj";
cout<< book1.title;
return 0;
}

#include<iostream>
using namespace std;
int main(){
   int numberGrid[2][6] = {


                 {1,2,4,5,6,7 },
                 {2,34,56,6,7,9}


            };
            for(int i=0;i<2;i++){

                for(int j =0; j<6; j++){

                    cout<< numberGrid[i][j];
                      cout<< endl;
                }



            }

return 0;
}



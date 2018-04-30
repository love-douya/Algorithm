#include <iostream>
using namespace std;

class A{
public:
    //A();
    //virtual ~A();
    int number = 1;
    const char* symbol = "b"; 
};

/*
struct B:public A{
public:
    B(int number):B_number(number){}
    int B_number;
    char symbol_B;
};
*/

int main(){
    A pp = {2, "a"};
    cout << "pp.number:" << pp.number << endl << "pp.symbol:" << pp.symbol << endl;//Tip: << is an overloaded operator which returns an object so that we can use <<A<<B<< ... <<C<<D
    //printf("pp.B_number:%d\npp.number:%d\npp.symbol_B:%s\n", pp.B_number, pp.number, pp.symbol_B);
}

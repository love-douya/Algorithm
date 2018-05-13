#include <iostream>
using namespace std;

class A{
public:
    A(){};
    virtual ~A(){};
    int b = 1; 
    const static int number;
    /*constexpr*/ static const char symbol = 'b'; 
};

const int A::number = 2;
//constexpr char A::symbol = 'a';

struct B:public A{
public:
    B(int number):B_number(number){}
    int B_number;
    char symbol_B;
};

//Other people's test
class CCC{
public:
	static const int a = 3; // Ok in C++11
	//static int b = 4;       // Error
	const int c = 5;        // Ok in C++11
	int d = 6;              // Ok in C++11
	CCC():c(0) { }     // Ok in C++11
};

int main(){
    CCC ob;
    cout << ob.a << endl;
    A pp;
    cout << pp.symbol << endl;
    //A pp = {2, "a"};
    //cout << "pp.number:" << pp.number << endl << "pp.symbol:" << pp.symbol << endl;//Tip: << is an overloaded operator which returns an object so that we can use <<A<<B<< ... <<C<<D
    //printf("pp.B_number:%d\npp.number:%d\npp.symbol_B:%s\n", pp.B_number, pp.number, pp.symbol_B);
    return 0;
}


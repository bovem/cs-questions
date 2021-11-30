#include <iostream>

using namespace std;

int main(){
    int a = 10;
    int *p;
    
    p = &a;

    cout<<"Value of a: "<<a<<endl;
    cout<<"Value of &a: "<<&a<<endl;
    cout<<"Value of p: "<<p<<endl;
    cout<<"Value of &p: "<<&p<<endl;
    cout<<"Value of *p: "<<*p<<endl;
    return 0;
}
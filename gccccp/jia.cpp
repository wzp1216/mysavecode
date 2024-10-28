#include <iostream>
using namespace std;

int main()
{
    long double a;
    long double b;
    char ch;
    cout<<"a:"<<endl;
    cin>>a;
    cout<<"b:"<<endl;
    cin>>b;
    cout<<"input +-*/:"<<endl;
    cin>>ch;
    
    switch (ch)
    {
    case '+':cout <<"a+b="<<a+b<<endl;
             break;
    case '-':cout <<"a-b="<<a-b<<endl;
             break;
    case '*':cout <<"a*b="<<a*b<<endl;
             break;
    case '/':cout <<"a/b="<<a/b<<endl;
             break;
    default:cout<<"error"<<endl;
    }
    return 0;

}

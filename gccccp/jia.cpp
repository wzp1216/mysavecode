#include <iostream>
using namespace std;

int main()
{
    unsigned long long a;
    unsigned long long b;
    char ch;
    cin>>a;
    cin>>b;
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

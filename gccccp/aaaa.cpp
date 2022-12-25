#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main()
{
    int a,b,c;
    char s1[]="2";
    char s2[]="3";
    a=atoi(s1);
    b=atoi(s2);
    c=a+b;
    cout<<c<<endl;
/*
    string s1,s2;
    s1="2";s2="3";
    a=stoi(s1);
    b=stoi(s2);
    c=a+b;
    cout<<c<<endl;
    int b;
    b=stoi('A')+stoi('B');
    cout<<b<<;
*/   
    return 0;
}
       

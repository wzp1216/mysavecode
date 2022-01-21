#include <iostream>

using namespace std;

int main()
{
    string myname {};
    myname="john";
    cout<<"please input a name:";
    getline(cin>>std::ws,myname);
    cout<<myname<<endl;

    return 0;
}


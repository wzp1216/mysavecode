#include <iostream>

using namespace std;

int main()
{
    int y=6;
    std::cout<<"this is starting ..."<<std::endl;
    {
        int x;
        std::cout<<"x="<<x<<endl;
    }
    std::cout<<y;
    

    return 0;
}


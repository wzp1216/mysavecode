#include <iostream>
#include <math>

using namespace std;

int main()
{
    int y{5};

    {
        int x;
        cin>>x;
        if (x==4) y=4;
    }
    cout<<y;
    

    return 0;
}


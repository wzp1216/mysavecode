#include <iostream>
#include <fstream>

using namespace std;
typedef struct record{
    int bushu;
    bool daka;
}record;

int main()
{
    FILE *fp;
    

    //read frist line;
    

    //read a[],b[];
    
    record a;
    a.bushu=100;
    a.daka=1;
    cout<<a.bushu<<" "<<a.daka<<endl;

    return 0;
}


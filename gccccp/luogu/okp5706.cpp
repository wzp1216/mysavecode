#include <iostream>
#include <iomanip>

using namespace std;
int  main()
{
    
    float all,t;
    int n,bei;
    cin>>all>>n;
    t=all/(n+0.0);
    cout<<setiosflags(ios::fixed)<<setprecision(3);
    cout<<t<<endl;
    cout<<n*2;

	return 0;
}


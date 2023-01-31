#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;
int  main()
{
    
    double a,b,c,p,s;
    cin>>a>>b>>c;
    p=0.5*(a+b+c);

    s=sqrt(p*(p-a)*(p-b)*(p-c));
    cout<<setiosflags(ios::fixed)<<setprecision(1);
    cout<<s;

	return 0;
}


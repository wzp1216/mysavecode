#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;
int  main()
{
    int s,v;
    int t,t2;
    int hh,tt;
    cin>>s>>v;
    t2=ceil(s*1.0/(v+0.0));
    t=t2+10;
    if (t>24*60) {
        cout<<"08:00";
        return 0;
    }

    hh=7-t/60;
    if (hh<0) hh=24+hh;
    tt=60-t%60;
    cout<<setw(2)<<setfill('0');
    cout<<hh<<":"<<tt;

    

	return 0;
}


H#include <iostream>
#include <cmath>
using namespace std;


int main(){
    
    int a[7],b[7],c[7];
    for (int i=0;i<7;i++) {
        cin>>a[i]>>b[i];
        if (a[i]+b[i]>8) 
            c[i]=a[i]+b[i]-8;
        else
            c[i]=0;
    }

    int imax,max=c[0];
    for (int i=0;i<7;i++) {
        if (c[i]>max){
            max=c[i]; imax=i;}
    }
    if (max>0)
        cout<<imax+1<<endl;
    else
        cout<<0<<endl;

    return 0;
}

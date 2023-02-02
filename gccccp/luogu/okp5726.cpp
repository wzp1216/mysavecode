#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    int n;cin>>n;
    int a[n];
    for(int i=0;i<n;i++) cin>>a[i];
    int nmin=10,nmax=0,imax,imin;
    float p;
    for(int i=0;i<n;i++){
       if(a[i]>nmax) {nmax=a[i];imax=i;}
       if(a[i]<nmin) {nmin=a[i];imin=i;}
    }
    a[imax]=0; a[imin]=0;
    int sum=0;
    for(int i=0;i<n;i++){
        sum=sum+a[i];
    }
    p=sum/(n-2.0);
    printf("%.2f",p);

}


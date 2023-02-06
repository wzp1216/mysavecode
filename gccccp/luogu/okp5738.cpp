#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;
bool zhi(int x){
    for (int i=2;i<=(x/2+1);i++)
        if (x%i==0) return 0;
    return 1;
}

int main(){
    int n;cin>>n;int s;
    int a[n];
    int len=0;
    for(int i=0;i<n;i++) {a[i]=0;}
    for(int i=0;i<n;i++) {
        cin>>s;
        if (zhi(s)){ a[i]=s;  len++;}
    }
    for(int i=0;i<n;i++) {
        if (a[i]!=0)
        cout<<a[i]<<" ";
    }

    return 0;
}

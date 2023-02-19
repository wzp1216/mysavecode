#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n;n=9;
    int a[n];int b[n];
    for(int i=0;i<n;i++){ cin>>a[i]; }
    for(int i=0;i<n;i++){ b[i]=a[i]; }

    for(int i=0;i<n;i++)
        for(int j=i;j<n;j++){
            b[i]=0;b[j]=0;
            int sum=0;
            for(int x=0;x<n;x++) sum+=b[x];
            if(sum==100)break;
            for(int x=0;x<n;x++) b[x]=a[x];
        }

    for(int i=0;i<n;i++){
        if(b[i]!=0) cout<<b[i]<<endl; 
    }

            return 0;
}



#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

bool zhi(int a){
    if(a==2) return 1;
    for (int i=2;i<a/2+1;i++)
        if (a%i==0) return 0;
    return 1;
}

int zhisum(int ge){
    int su=2,i=0,sum=2;
    while(1){
     if (zhi(su)){
        sum+=su;
        i++;
     }
     if (i==ge) break;
    }
    return sum;
}



int main(){
    int n;    cin>>n;
    if (n<2) {cout<<0;return 0;}
    if (n==2) {cout<<2<<endl;cout<<1;return 0;}
    int sum; sum=0;
    int i=2; int ge=0;
    while(sum<n){
        if (zhi(i)) {
            sum+=i;
            if(sum<=n) cout<<i<<endl;
            ge++;
            if(sum>n) ge--;
        }
        i++;
    }
    cout<<ge<<endl;
   return 0;
}

#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n;cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int lian=0,amax=0;
    for(int i=0;i<n;i++){
        if ((a[i+1]-a[i])==1) {
            lian++;
            if (lian>amax) amax=lian;
        }
        else {

            lian=0;
        }
    }
    cout<<amax+1;


   
   
    return 0;
}

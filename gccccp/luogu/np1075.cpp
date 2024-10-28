#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

bool zhisu(int a){
    if (a==2) return 1;
    if (a==3) return 1;
    for(int i=2;i<a/2+1;i++)
        if (a%2==0) return 0;
    return 1;
}

int main(){
    int n;cin>>n;
    int size=n/2+1;
    int zhi[size];
    for(int i=0;i<size;i++) zhi[i]=0;
    //find all zhisu;
    for(int i=0;i<size;i++){
        for(int zh=2;zh<size;zh++)
            if (zhisu(zh) && n%zh==0)
                zhi[i]=zh;
    }

    //find max;   
    int nmax=2;
    for(int i=0;i<size;i++){
        if (zhi[i]>nmax) nmax=zhi[i];
    }
    cout<<nmax;

   
    return 0;
}

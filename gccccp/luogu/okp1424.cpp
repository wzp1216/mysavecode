#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

int t[7]={0,250,250,250,250,250,0};

int main(){
  
    int x,n,all;
    cin>>x>>n;
    all=0;
    for(int i=x;i<x+n;i++){
        all+=t[i%7];
        //cout<<all<<endl;

    }
    cout<<all;



    
    return 0;
}

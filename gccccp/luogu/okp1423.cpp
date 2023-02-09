#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    float all,sum=0,bujuli=2.0;
    int bushu=1;
    cin>>all;
    if(all<=2) { cout<<1;return 0;}
    sum=2;
    while(1){
        bujuli=bujuli*0.98;
        sum+=bujuli;
        bushu++;
        if (sum>=all) break;
    }
    cout<<bushu<<endl;

    return 0;
}



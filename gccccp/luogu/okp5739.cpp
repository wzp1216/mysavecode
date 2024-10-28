#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int jiechen(int x){
    int y=0;
    if(x>2) y=x*jiechen(x-1);
    else if(x==2) y=2;
    else if(x==1) y=1;
    return y;
}

int main(){
    int n;cin>>n;
    cout<<jiechen(n);

            return 0;
}



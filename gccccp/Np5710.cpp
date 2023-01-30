#include <iostream>
#include <cmath>
using namespace std;

bool T1(int a){
    if (a%2==0)
        return 1;
    else 
        return 0;
}

bool T2(int a){
    if ((a>4)&&(a<=12))
        return 1;
    else 
        return 0;
}

int main(){
    
    // a%2==0  >4 <12;
    int n;
    cin>>n;
    bool a,b;
    a=T1(n);b=T2(n);
    cout<<a&&b;
    cout<<' ';
    cout<<a||b;
    cout<<' ';
    cout<<(a&&!b)||(b&&!a)||(a&&b);
    cout<<' ';
    cout<<(!a)&&(!b);



    return 0;
}

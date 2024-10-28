#include <iostream>
#include <cmath>
using namespace std;

bool leap(int n){
    if (n%400==0)  return 1;
    if ((n%4==0)&&(n%100!=0)) return 1;
    return 0;
}



int main(){
    
    int n;
    cin>>n;
    cout<<leap(n)<<endl;
    

    return 0;
}

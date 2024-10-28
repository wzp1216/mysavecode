#include <iostream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <ctime>
using namespace std;

bool zhi(int a){
    if(a==2) return 1;
    if (a%2==0) return 0;
    for (int i=3;i<=sqrt(a);i+=2){
        if (a%i==0) return 0;
        }
    return 1;
}

bool huiwen(int n){
    int x=n,y=0;
    int wei=n%10;
    if (n>10 && wei!=1 && wei!=3 && wei!=7 && wei!=9) return 0;
    while(x>0){
        y=y*10+x%10;
        x/=10;
    }
    return y==n;
}

int main(){
    int a,b;
    cin>>a>>b;
    //clock_t starttime,endtime;
    //starttime=clock();

    if (a%2==0) a++;
    for(int i=a;i<=b;i=i+2){
        if (huiwen(i)) {
            if (zhi(i))   cout<<i<<endl;
        }
    }
    
    //endtime=clock();
    //cout<<"time is "<<endtime-starttime<<endl;
  return 0;
}

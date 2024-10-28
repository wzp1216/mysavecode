#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    int n;n=12;
    int a[n];
    int mama[12]={};
    for(int i=0;i<n;i++) cin>>a[i];
    int yu=0;
    bool qian=0;
    for(int i=0;i<n;i++){
        yu=yu+300-a[i];
        if(yu<0) { cout<<"-"<<i+1<<endl; qian=1;break;}
        if(yu>=100){
            mama[i]=(yu/100)*100;
        }
//        cout<<yu<<"-"<<mama[i]<<"="<<yu-mama[i]<<endl;
        yu=yu-mama[i];
    }
if(!qian){
    int ss=0;
    for(int i=0;i<n;i++){ss=ss+mama[i];}
    int year=yu+ss/5+ss;
    cout<<year<<endl;
}

}


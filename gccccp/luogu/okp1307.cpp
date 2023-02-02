#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int num,fan;
    string stzhe,stfan;
    stringstream ss;
    cin>>num;
    ss<<num;ss>>stzhe;ss.clear();
    for(auto it=stzhe.end()-1;it!=stzhe.begin();it--)
       ss<<*it;
    ss<<*stzhe.begin();
    ss>>stfan;
    if(num>0) {
        ss.clear();
        ss<<stfan;ss>>fan;
        cout<<fan;
    }
    else {
        *(stfan.end()-1)=0;
        ss.clear();
        ss<<stfan;ss>>fan;
        cout<<"-"<<fan;
    }
    return 0;
}



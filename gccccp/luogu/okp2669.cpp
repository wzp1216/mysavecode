#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int maxday;
    cin>>maxday;
    int sum=0,jb=1,ci=0;
    int day=1;
    while(1){
            sum+=jb;
            ci++;
            day++;
            if(ci==jb){jb++; ci=0;}
//            cout<<"day:"<<day<<"jb:"<<jb<<"ci"<<ci<<endl;
//            cout<<"sum:"<<sum<<endl;
        if(day>maxday) {cout<<sum;break;}
    }
    return 0;
}

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(){
    int a,b;cin>>a>>b;
    std::stringstream ss;
    string all;
    int ge[10];
    for (int i=0;i<10;i++) ge[i]=0;
    for( int i=a;i<=b;i++)
        ss<<i;
    ss>>all;
    int len=all.size();
    for (int i=0;i<len;i++){
        char ch=all[i];
        int x;
        if ((ch>='0')&&(ch<='9')) {
            ss.clear();
            ss<<ch; ss>>x;
            ge[x]++;
        }
    }
    for (int i=0;i<10;i++){
        cout<<ge[i]<<" ";
    }


    return 0;
}


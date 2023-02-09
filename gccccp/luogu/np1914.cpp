#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n;cin>>n;
    string st;
    cin>>st;
    int len=st.size();
    for(int i=0;i<len;i++){
        st[i]=st[i]+n;
        if(st[i]>'z') st[i]='a'+st[i]-'z'-1;
    }
    cout<<st;
    
        return 0;
}



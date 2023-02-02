
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n,k=0;
    char ch;
    cin>>n>>ch;
    std::stringstream ss;
    string st;
    for(int i=1;i<=n;i++)
        ss<<i;
    ss>>st;ss.clear();
//    cout<<st<<endl;
    int len=st.size();
    for(int i=0;i<len;i++){
        if(st[i]==ch) k++;
    }
    cout<<k<<endl;
    
    return 0;
}

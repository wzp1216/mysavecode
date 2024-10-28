#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;


int main(){
    
    vector<int> v;
    for (int i=0;i<3;i++){
        int n;
        cin>>n;
        v.push_back(n);
    }
    sort(v.begin(),v.end());
    int a=*v.begin();
    int b=*(v.begin()+1);
    int c=*(v.end()-1);

    string st;
    cin>>st;

    for (int i=0;i<3;i++){
        char ch=st[i];
        if (ch=='A') cout<<a<<' ';
        if (ch=='B') cout<<b<<' ';
        if (ch=='C') cout<<c<<' ';
    }
    
    
 
    
    return 0;
}

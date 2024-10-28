#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    vector <int> v;
    int n;cin>>n;
    for(int i=0;i<n;i++) {
        int x;cin>>x;
        v.push_back(x);
    }
    
    int s=0;
    sort(v.begin(),v.end());
    for (auto a=v.begin();a!=v.end()-2;a++){
        for(auto b=a+1;b!=v.end()-1;b++)
            for(auto c=b+1;c!=v.end();c++){
                if((*a+*b)==*c) {
                    s++;
                    cout<<s<<"-"<<*a<<"-"<<*b<<"-"<<*c<<endl;
                }
            }
    }

    cout<<s;


    
    return 0;
}

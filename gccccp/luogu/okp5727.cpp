#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    vector <int> v;
    int n;cin>>n;
    v.push_back(n);
    while (n!=1){
        if(n%2==0) n=n/2;
        else n=n*3+1;
        v.push_back(n);
    }
    
    for (auto it=v.end()-1;it!=v.begin();it--)
        cout<<*it<<" ";
    cout<<*v.begin();

    return 0;
}


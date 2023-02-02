#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    vector <int> v;
    int n=1;
    while (n!=0){
        cin>>n;
        v.push_back(n);
    }
    for(auto it=v.end()-2;it!=v.begin();it--)
        cout<<*it<<" ";
    cout<<*v.begin();

    return 0;
}


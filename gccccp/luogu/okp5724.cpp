#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){

    vector <int> v;
    int n;cin>>n;
    int a;
    for(int i=0;i<n;i++) {
        cin>>a;
        v.push_back(a);
    }
    sort(v.begin(),v.end());
    a=*(v.end()-1)-*v.begin();
    cout<<a;


    
   
    return 0;
}

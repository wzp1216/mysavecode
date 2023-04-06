#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n,m;cin>>n>>m;
    int a[n];
    for(int i=0;i<n;i++) {
        cin>>a[i];
    }
    vector<int> v;
    for(int i=0;i<=n-m;i++) {
        int sum=0;
        for(int j=0;j<m;j++){
            sum+=a[i+j];
        }
        v.push_back(sum);
    }
    sort(v.begin(),v.end());
    cout<<*v.begin();

}

#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    int l,m;
    cin>>l>>m;
    int u[m],v[m];
    int sum=0;
    for(int i=0;i<m;i++) {
        cin>>u[i]>>v[i];
        sum=sum+v[i]-u[i]+1;
    }
    cout<<l-sum;
    return 0;
}


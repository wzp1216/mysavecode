#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    int l,m,u,v;
    cin>>l>>m;
    int a[l+1];
    for(int j=0;j<l+1;j++) a[j]=1;
    for(int i=0;i<m;i++) {
        cin>>u>>v;
        for(int j=u;j<v+1;j++)
            a[j]=0;
    }
    int sum=0;
    for(int j=0;j<l+1;j++) if (a[j]==1) sum++;
    cout<<sum;
    return 0;
}


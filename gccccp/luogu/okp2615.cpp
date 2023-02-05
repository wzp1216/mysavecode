#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n; cin>>n;
    int a[n][n];
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            a[i][j]=0;
    int i=0;int j=n/2;
    a[i][j]=1;
    for(int x=2;x<=n*n;x++){
        if ((i==0)&&(j==(n-1))) 
            {i=1;j=n-1;a[i][j]=x;continue;}
        i--;j++;   //1,2--0,3
        if (i==(-1)) i=n-1;
        if (j==n) j=0;
        if (a[i][j]==0) {a[i][j]=x;}
        else {i=i+2;j--;a[i][j]=x;}
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
            cout<<a[i][j]<<" ";
        cout<<endl;
        }
        
    return 0;
}

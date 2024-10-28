#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(){
    int n; cin>>n;
    int a[n][n];
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            a[i][j]=0;
    a[0][0]=1; a[1][0]=1;a[1][1]=1;
    for(int i=2;i<n;i++){
        for(int j=0;j<n;j++){
            if (j==0) a[i][j]=1;
            else if (j==i) a[i][j]=1;
            else a[i][j]=a[i-1][j-1]+a[i-1][j];
        }
    }

            
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
            if(a[i][j]!=0) cout<<a[i][j]<<" ";
        cout<<endl;
    }

    return 0;
}


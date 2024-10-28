#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    int n; cin>>n;
    int a[n][4];
    for (int i=0;i<n;i++){
        for(int j=0;j<3;j++)
            cin>>a[i][j];
        a[i][3]=a[i][0]+a[i][1]+a[i][2];
    }
    int sum=0; 
    for (int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if ( (abs(a[i][0]-a[j][0])<=5) &&  (abs(a[i][1]-a[j][1])<=5) && (abs(a[i][2]-a[j][2])<=5)  &&  (abs(a[i][3]-a[j][3])<=10) )  sum++;
        }
    }

   cout<<sum;
    return 0;
}


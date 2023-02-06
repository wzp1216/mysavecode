#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
using namespace std;

int main(){
    int n,m;  //n--students   m--scores;
    cin>>n>>m;
    int fen[m];
    float sum[n],allmax=0;
    for(int j=0;j<n;j++) sum[j]=0;
for(int j=0;j<n;j++){
    int max=0,min=10;
    for(int i=0;i<m;i++){
        cin>>fen[i];
        sum[j]=sum[j]+fen[i];
        if (fen[i]>max) max=fen[i];
        if (fen[i]<min) min=fen[i];
    }
    sum[j]=(sum[j]-max-min+0.0)/(m-2.0);
    if (sum[j]>allmax) allmax=sum[j];
}
    printf("%.2f",allmax);
    return 0;
}

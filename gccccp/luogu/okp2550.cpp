#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

void psort(int *a){
    vector <int> v;
    for(int i=0;i<7;i++)
        v.push_back(*(a+i));
    sort(v.begin(),v.end());
    for(int i=0;i<7;i++)
        *(a+i)=*(v.begin()+i);
}

int main(){
    int n; cin>>n;
    int jiang[7];
    for (int i=0;i<7;i++) cin>>jiang[i];
    int piao[n][7];
    for(int i=0;i<n;i++)
        for(int j=0;j<7;j++)
            cin>>piao[i][j];
       int zh[7]={};
    for(int i=0;i<n;i++){
        int zhongsu=0;
        for(int j=0;j<7;j++){
            for( int k=0;k<7;k++){
            if (piao[i][j]==jiang[k]){
                zhongsu++;
            }
            }
        }
        if (zhongsu>0) zh[zhongsu-1]++;
    }
    for(int i=6;i>=0;i--) cout<<zh[i]<<" ";
}


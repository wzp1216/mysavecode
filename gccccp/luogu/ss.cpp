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
    psort(jiang);
    for(int i=0;i<n;i++) psort(piao[i]);

    for(int i=0;i<7;i++) cout<<jiang[i]<<"-";
    cout<<endl;
    for(int i=0;i<7;i++) cout<<piao[0][i]<<"-";
    cout<<endl;
    for(int i=0;i<7;i++) cout<<piao[1][i]<<"-";
    cout<<endl;
    int zh[8]={};
    for(int i=0;i<n;i++){
        int zhosu=0;
        for(int j=0;j<7;j++){
            if (piao[i][j]==jiang[j]){
                zhosu++;
                if (piao[i][j]>jiang[j]) break;
            }
        }
        if (zhosu>0) zh[zhosu]++;
    }
    for(int i=0;i<8;i++) cout<<zh[i]<<" ";

                    

}


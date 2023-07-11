#include <iostream>
using namespace std;

int main()
{
    int n,m;cin>>n>>m;
    int piao;
    int houxuan[n];
    for(int j=0;j<n;j++) houxuan[j]=0;
    int i=0;
    // read m  piao;
    while(m--){cin>>piao;i++;
        houxuan[piao-1]++;
    }

    for(int j=0;j<n;j++){
        for(int i=0;i<houxuan[j];i++)
            cout<<j+1<<" ";  //有几张票，输出几次
    } 

    return 0;
}


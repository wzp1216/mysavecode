#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;
struct ROAD{
    int A;
    int B;
    int t;
};

int main(){
    //村庄数V   公路数R  公路双向 修好路所用时间t 
    //read from file title.in
    //4 4
    //1 2 6
    //1 4 4 
    //1 4 5
    //4 2 3
    freopen("title.in","r",stdin);
    int village,road;
    cin>>village>>road;
    int V[village],V_all[road*2];
    ROAD R[road];
    for(int i=0;i<road;i++){
        cin>>R[i].A>>R[i].B>>R[i].t;
        if (R[i].A>R[i].B)
        {int tmp=R[i].A;R[i].A=R[i].B;R[i].B=tmp;}
        V_all[i]=R[i].A;
        V_all[i+road]=R[i].B;
    }
    
    sort(V_all,

    for(int i=0;i<road;i++)
        cout<<R[i].A<<" "<<R[i].B<<" "<<R[i].t<<endl;


    return 0;
}



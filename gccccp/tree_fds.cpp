#include <cstdio>
#include <iostream>
using namespace std;
int value[260],winner[260];
int n ;

void dfs(int x){
    if (x>= 1<<n) return; 
    else{
        dfs(2*x);
        dfs(2*x+1);
        int lvalue=value[2*x],rvalue=value[2*x+1];
        if (lvalue>rvalue){
            value[x]=lvalue;
            winner[x]=winner[2*x];
        } else {
            value[x]=rvalue;
            winner[x]=winner[2*x+1];
        }
    }
}

int main(){
    cin>>n;
    for(int i=0;i<1<<n;i++){
        cin>>value[i+(1<<n)];
        winner[i+(1<<n)]=i+1;
    }
    dfs(1);
    cout<<((value[2]>value[3]) ? winner[3]:winner[2]);

    for(int i=0;i<1<<n;i++){
        cout<<winner[i]<<"--";
        //cout<<(i+1<<n) <<"-"<<winner[i+(1<<n)]<<"--";
    }
    return 0;

}



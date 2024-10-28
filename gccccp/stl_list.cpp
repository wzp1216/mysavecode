#include <cstdio>
#include <list>
#include <iostream>

using namespace std;
int main(){
    list <int> l1;
    int n,tmp,a,b;
    cout<<"input list lenght:";
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        cin>>tmp;
        l1.push_back(tmp);
    }
    cout<<"input a to b:"<<endl;
    cin>>a>>b;
    list <int>::iterator it;
    for(it=l1.begin();it!=l1.end();it++){
        if (*it==a) *it=b;
    }
    for(it=l1.begin();it!=l1.end();it++){
        cout<<*it;
    }
    cout<<endl;
    return 0;
}





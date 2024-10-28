#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
struct coin{
    int m,v;
} a[20];
bool cmp(coin x,coin y){
    return x.v*y.m>y.v*x.m;
}

int main(){
    freopen("title.in","r",stdin);
    int n,t,c,i;
    float ans=0;
    std::cin>>n>>t; //all number=n;  all m=t;
    cout<<n<<"--"<<t<<"g"<<endl;
    c=t;
    for(i=0;i<n;i++)
        cin>>a[i].m>>a[i].v;  //mg;  value;
    sort(a,a+n,cmp);
    cout<<"-----------"<<endl;
    for(i=0;i<n;i++)
        cout<<a[i].m<<"g---"<<a[i].v<<endl;  //mg;  value;
    cout<<"-----------"<<endl;
    for(i=0;i<n;i++){
        if (a[i].m>c) continue;
        c-=a[i].m;
        cout<<i<<":"<<a[i].m<<"-"<<a[i].v<<endl;
        ans+=a[i].v;
    }
    printf("%.2lf",ans);

    


    return 0;
}


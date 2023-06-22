#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

void qsort(long int a[] , int l, int r){
    long int i=l,j=r,flag=a[(l+r)/2],tmp;
    do{
        while(a[i]<flag) i++;  //从左向右，找比哨兵小的数
        while(a[j]>flag) j--;  //从右，找比哨兵小的
        if(i<=j){
            tmp=a[i];a[i]=a[j];a[j]=tmp;
            i++;j--;
        }
    }while(i<=j);
    if(l<j) qsort(a,l,j);
    if(i<r) qsort(a,i,r);
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("title.in","r",stdin);
        freopen("title.out","w",stdout);
    #endif
    int n;    cin>>n;
    long int a[n];
    for(int i=0;i<n;i++) cin>>a[i];
    qsort(a,0,n);
    for(int i=0;i<n;i++) cout<<a[i]<<" ";

    return 0;
}


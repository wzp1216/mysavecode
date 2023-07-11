#include <iostream>
using namespace std;

int main()
{
    int n;cin>>n;
    int a[n],tmp;
    int key;
    for(int i=0;i<n;i++) cin>>a[i];
    for(int i=0;i<n;i++) {
        key=a[i];
        for(int j=n-1;)


        tmp=a[i];a[j]=a[j];a[j]=tmp;
    }
    

    return 0;
}


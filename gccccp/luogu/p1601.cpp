// add two num 500
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

#define maxn 520
int a[maxn],b[maxn],c[maxn];
int main(){
    string A,B;
    cin>>A>>B;
    int len=max(A.length(),B.length());
    for (int i=A.length()-1,j=1;i>=0;i--,j++)
        a[j]=A[i]-'0';
    for (int i=B.length()-1,j=1;i>=0;i--,j++)
        b[j]=B[i]-'0';
    for (int i=1;i<=len;i++){
        c[i]+=a[i]+b[i];
        c[i+1]=c[i]/10;
        c[i]%=10;
    }
    for (int i=0;i<=A.length();i++) cout<<a[i];
    for (int i=0;i<=B.length();i++) cout<<b[i];
    cout<<endl;

    if(c[len+1]) len++;
    for (int i=len;i>=1;i--)
        cout<<c[i];
}




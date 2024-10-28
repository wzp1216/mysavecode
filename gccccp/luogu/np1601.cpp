#include <iostream>
#include <sstream>
#include <string>
using namespace std;
int main(){
    string astr,bstr;
    cin>>astr>>bstr;
    int a[510]={};int b[510]={},c[510]={};
    int lena=astr.size(), lenb=bstr.size();
    int lenc; lenc=lena>lenb?lena:lenb; lenc+=2;
    for(int i=0;i<lena;i++) a[i]=astr[i]-'0';
    for(int i=0;i<lenb;i++) b[i]=bstr[i]-'0';
    for(int i=lenc-1;i>=0;i--){
        if(i>(lenc-lena-1)) a[i]=a[i+lena-lenc];
        else a[i]=0;
        if(i>(lenc-lenb-1)) b[i]=b[i+lenb-lenc];
        else b[i]=0;
    }
    int he, j=0;
    for(int i=lenc-1;i>=0;i--){
        he=a[i]+b[i]+j;
        c[i]=he%10;
        j=he/10;
    }
    bool xian=0;
    for(int i=0;i<lenc;i++){
        if (c[i]!=0) xian=1;
        if (xian) cout<<c[i];
    }
        return 0;
}

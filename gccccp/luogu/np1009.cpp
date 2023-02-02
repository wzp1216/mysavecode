#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;

#define maxn 200
string bigadd(string A,string B){
    int a[maxn],b[maxn],c[maxn];
    for (int i=0;i<200;i++) c[i]=0;
    int len=max(A.length(),B.length());
    for (int i=0;i<=len+1;i++) a[i]=0;
    for (int i=0;i<=len+1;i++) b[i]=0;
    for (int i=A.length()-1,j=1;i>=0;i--,j++)
        a[j]=A[i]-'0';
    for (int i=B.length()-1,j=1;i>=0;i--,j++)
        b[j]=B[i]-'0';
    for (int i=1;i<=len;i++){
        c[i]+=a[i]+b[i];
        c[i+1]=c[i]/10;
        c[i]%=10;
    }
    std::stringstream ss;
    ss.clear();    string C;
    if(c[len+1]) len++;
    for (int i=len;i>=1;i--)
        ss<<c[i];
    ss>>C;ss.clear();
    return C;
}

string jiecheng(int a){
    string num; std::stringstream ss;
    long long s=1;
    for(int i=1;i<=a;i++)
        s=s*i;
    ss.clear();  ss<<s;
    ss>>num;ss.clear();
    return num;
}

int main(){
    int n;  cin>>n;
    string st;
    st="0"; 
    for (int i=1;i<=n;i++){
        //cout<<i<<"!="<<jiecheng(i)<<endl;
        st=bigadd(jiecheng(i),st);
    }
    cout<<st<<endl;

    return 0;
}




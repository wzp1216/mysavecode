
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;

#define maxn 100

class Bigint{
    public:
    Bigint(int x=0){
        memset(a,0,sizeof(a));
        for(len=1;x;len++)
            a[len]=x%10,x/=10;
        len--;
    }
    
    private:
    int len,a[maxn];
    int &operator[](int i){
        return a[i];
    }
    void flatten(int L){
        this->len=L;
        for (int i=1;i<=this->len;i++)
            a[i+1]=a[i]/10,a[i]%=10;
        for(;!a[this->len]; )
            this->len--;
    }
    void print(){
        for(int i=max(len,1);i>=1;i--)
            printf("%d",a[i]);
    }
    operator+(Bigint a,Bigint b){
        Bigint c;
        int len=max(a.len,b.len);
        for (int i=1;i<=len;i++)
            c[i]+=a[i]+b[i];
        c.flatten(len+1);
        return c;
    }
    
    operator*(Bigint a,int b){
        Bigint c;
        int len=a.len;
        for (int i=1;i<=len;i++)
            c[i]=a[i]*b;
        c.flatten(len+11);
        return c;
    }
};

int main()
{
    Bigint ans(2342),fac(9);
    /*
    int m;
    cin>>m;
    for(int i=1;i<=m;i++){
        fac=fac*i;
        ans=ans+fac;
    }
    */
    fac=ans*2;
    ans.print();
    fac.print();
}

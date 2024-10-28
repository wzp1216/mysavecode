
#include <iostream>
#include <cstdio>


using namespace std;


__int128 read(){
    __int128 x=0,f=1;
    char ch=getchar();
    while(ch<'0' || ch>'9'){
        if (ch=='-') f=-1;
        ch=getchar();
    }
    while(ch>='0'&& ch<='9'){
        x=x*10+ch-'0';
            ch=getchar();
    }
    return x*f;
}
void print(__int128 x){
    if(x<0){
        putchar('-');
        x=-x;
    }
    if(x>9) print(x/10);
    putchar(x%10+'0');
}

int main(){
    __int128 longinta,longintb;
    longinta=read();
    longintb=read();
    __int128 xx=longinta/longintb;
    print(longinta);
    putchar('\n');
    print(longintb);
    putchar('\n');
    print(xx);

    return 0;
}



#include <stdio.h>
#include <cstdio>
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    char a[101],s[101];
    int i,len,mid,next,top;
    std::fgets(a,sizeof(a),stdin);
    len=strlen(a);
    cout<<len<<endl;
    len--;
    mid=len/2-1;
    top=0;
    for(i=0;i<=mid;i++) s[++top]=a[i];
    if(len%2==0) next=mid+1;
    else next=mid+2;
    for(i=next;i<=len-1;i++)
    {
        if(a[i]!=s[top]) break;
        top--;
    }
    if(top==0) printf("yes\n");
    else printf("no\n");
    return 0;
}


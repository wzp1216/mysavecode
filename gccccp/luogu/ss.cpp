Hkkjk#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
struct point{
    int x;int y;int z;};
struct line{
    point a;point b;};

int main(){
    int length,width,height; cin>>length>>width>>height;
    int n; cin>>n;
    line ll[n];
    for(int i=0;i<n;i++){
        line l;
        cin>>l.a.x>>l.a.y>>l.a.z>>l.b.x>>l.b.y>>l.b.z;
        ll[i]=l;
    }
   
    int a[length][width][height];
    for(int i=0;i<length;i++)
         for(int j=0;j<width;j++)
            for(int k=0;k<height;k++)
                a[i][j][k]=1;
    for(int x=0;x<n;x++){
        line l=ll[x];
    for(int i=l.a.x;i<=l.b.x;i++)
         for(int j=l.a.y;j<=l.b.y;j++)
            for(int k=l.a.z;k<=l.b.z;k++)
                a[i][j][k]=0;
    }
   int sum=0;
    for(int i=0;i<length;i++)
         for(int j=0;j<width;j++)
            for(int k=0;k<height;k++)
                sum=sum+a[i][j][k];
    cout<<sum<<endl;
    return 0;
}


#include <iostream>
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
    point pa=ll[x].a,pb=ll[x].b;
    for(int i=0;i<length;i++)
         for(int j=0;j<width;j++)
            for(int k=0;k<height;k++){
                if (i>=pa.x && i<=pb.x && j>=pa.y && j<=pb.y &&  k>=pa.z && k<=pb.z  )
                a[i][j][k]=0;
                }
    }
    int sum=0;
    for(int i=0;i<length;i++)
         for(int j=0;j<width;j++)
            for(int k=0;k<height;k++)
                if (a[i][j][k]==1) sum++;
    cout<<sum<<endl;
    return 0;
}


#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
int const MAXIN=50;
struct student{
    int id;
    int chinese;
    int math;
    int english;
    int total;
};
student a[MAXIN];
int cmp(student a,student b){
    if (a.total!=b.total) return a.total>b.total;
    if (a.chinese!=b.chinese) return a.chinese>b.chinese;
    return a.id>b.id;
}

int main(){
    freopen("title.in","r",stdin);
    int n;
    cin>>n;
    for (int i=0;i<n;i++){
        std::cin>>a[i].id>>a[i].chinese>>a[i].math>>a[i].english;
        a[i].total=a[i].chinese+a[i].math+a[i].english;
    }
    sort(a,a+n,cmp);
    for (int i=0;i<n;i++){
        std::cout<<a[i].id<<" "<<a[i].total<<" "<<a[i].chinese<<" "<<a[i].math<<" "<<a[i].english<<endl;
    }


    return 0;
}


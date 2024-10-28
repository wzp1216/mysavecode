#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

struct chengji{
    string name;
    int yuwen;
    int shuxue;
    int eng;
};

int main(){
    int n;cin>>n;
    chengji a,b;
    int x=0,sum=0;
    for(int i=0;i<n;i++){
        cin>>a.name>>a.yuwen>>a.shuxue>>a.eng;
        sum=a.yuwen+a.shuxue+a.eng;
        if (sum>x) {x=sum;b=a;}
    }
    cout<<b.name<<" "<<b.yuwen<<" "<<b.shuxue<<" "<<b.eng;




    return 0;
}



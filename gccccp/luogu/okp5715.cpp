#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;



int main(){

    int a[3];
    cin>>a[0]>>a[1]>>a[2];
    
    std::vector<int> myvector (a,a+3);
    sort(myvector.begin(),myvector.end());
    for (auto it=myvector.begin();it!=myvector.end();++it)
        cout<<*it<<" ";

    return 0;
}

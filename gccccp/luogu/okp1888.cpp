#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int main(){
    //a[3]  sort ;
    int l[3];
    cin>>l[0]>>l[1]>>l[2];

    vector<int> v(l,l+3);
    sort(v.begin(),v.end());

    int a=*v.begin();int b=*(v.end()-1);
    // cout<<a<<b<<endl;
    for (int i=1;i<=a;i++)
        if (a%i==0 && b%i==0)
        {a=a/i;b=b/i;
        //   cout<<a<<b<<endl;
        }
    cout<<a<<"/"<<b<<endl;

  
    
    return 0;
}

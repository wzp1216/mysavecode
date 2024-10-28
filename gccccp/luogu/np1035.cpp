
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int k;
    cin>>k;
    int i=1;float sum=0;
    while(sum<=k){
       sum+=1.0/i;
//       cout<<sum<<endl;
//       cin.get();
       i++;
    }
    cout<<i-1<<endl;
   
    return 0;
}

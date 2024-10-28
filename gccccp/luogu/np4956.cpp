#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    int n;cin>>n;
    int x;    x=(n/52-21)/7;
    int k=1,sum=(7*x+21*k)*52;
    if(x>100){
        k=(n/52-700)/21;
        sum=(7*x+21*k)*52;
    }
    while (1) {
        if (sum==n) break;
        k++;
        x=(n/52-21*k)/7;
        sum=(7*x+21*k)*52;
    }
    cout<<x<<endl<<k<<endl;
}


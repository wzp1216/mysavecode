#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
    int n;
    cin>>n;

    int k=n;
    int p=1;
    for(int i=n;i>=0;i--){
        for(int j=1;j<=k;j++){
            if (p<10) cout<<"0"<<p;
            else cout<<p;
            p++;
        }
        cout<<endl;
        k--;
    }


   
    return 0;
}

#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n;cin>>n;
    string st1[n],str2[n];
    stringstream ss;
    int j=0;
    for(int i=1;i<=n*n;i++){
        if (i<10) ss<<"0"<<i;
        else ss<<i;
        if (i%n==0){
           ss>>st1[j];ss.clear();
           j++;
        }
    }
    for( int i=0; i<j;i++)
        {cout<<st1[i];  cout<<endl;}
    cout<<endl;
    
    j=n; ss.clear();int da=1;
    for(int x=0;x<n;x++){
        for(int k=0;k<j;k++)
        {ss<<"  ";}
        j--;
        for(int s=0;s<n-j;s++){
            if (da<10) ss<<"0"<<da;
            else ss<<da;
            da++;
        }
        ss<<endl;
        ss>>str2[x];ss.clear();
        if (j==0) break;
    }
    cout<<std::right;
    for( int i=0; i<n;i++)
        {cout<<std::setw(2*n)<<str2[i];  cout<<endl;}



    return 0;
}

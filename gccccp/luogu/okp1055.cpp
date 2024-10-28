#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    string bn;
    std::stringstream ss;
    cin>>bn;
    int l=bn.size();
    int a[10];
    int j=0;
    for (int i=0;i<l;i++){
        if (i==1 || i==5 || i==11) continue;
        string s;
        ss<<bn[i];ss>>s;ss.clear();
//        cout<<s<<endl;
        try{
        a[j]=stoi(s);j++;
        }
        catch (...){
            continue;
        }
    }
    int sum=0;
    for (int j=0;j<9;j++){
        sum=sum+a[j]*(j+1);
    }
    int  jiaoyan=sum%11;
    char jiaoyanch;
    ss.clear();ss<<jiaoyan;ss>>jiaoyanch;ss.clear();
    if (jiaoyan==10) jiaoyanch='X';
    if (bn[12]==jiaoyanch)
       cout<<"Right"; 
    else if (jiaoyan==10 && bn[12]=='X')
       cout<<"Right"; 
    else {
        bn[12]=jiaoyanch;
        cout<<bn;
    }
 
    
    return 0;
}

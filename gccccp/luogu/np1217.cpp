#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

bool zhi(int a){
    if(a==2) return 1;
         if (a%2==0 && a!=2) return 0;
        else if (a%3==0&& a!=3) return 0;
        else if (a%5==0&& a!=5) return 0;
        else if (a%7==0&& a!=7) return 0;
        else if (a%11==0&& a!=11) return 0;
        else if (a%13==0&& a!=13) return 0;
        else if (a%17==0&& a!=17) return 0;
        else if (a%19==0&& a!=19) return 0;
        else {
        for (int i=23;i<a/2;i++)
        if (a%i==0) return 0;
        }
    return 1;
}

bool huiwen(int a){
    std::stringstream ss;
    string str,stdao;
    ss<<a;  ss>>str;
    ss.clear();
    for (auto it=str.end()-1; it!=str.begin();it--)
        ss<<*it;
    ss<<*str.begin();
    ss>>stdao; 
    int dao=stoi(stdao);
    if (a==dao) return 1;
    else return 0;
}

int main(){
    int a,b;
    cin>>a>>b;
    for(int i=a;i<=b;i++){
       bool a=zhi(i);
        if (a) {
            bool b=huiwen(i);
            if (b){
                cout<<i<<endl;
            }
        }
    }
    
  return 0;
}

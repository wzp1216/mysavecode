#include <iostream>
#include <sstream>
#include <string>
using namespace std;
int main(){
    string str[4];
    int a[26]={};
    for (int i=0; i<4;i++){
        std::getline(std::cin,str[i]);
        int len=str[i].size();
        for(int j=0;j<len;j++){
            int x=str[i][j]-'A';
            if ((x>=0)&&(x<=26)) a[x]++;
        }
    }
    int max=0;
    for (int i=0;i<26;i++){
        //cout<<a[i]<<"*";
        if (a[i]>max) max=a[i];
    }
    int tu[max][26];
    for(int i=max-1;i>=0;i--){
        for (int j=0;j<26;j++){
            if(i>=(max-a[j])) tu[i][j]=1;
            else tu[i][j]=0;
        }
    }
    string tmp;
    for(int i=0;i<max;i++){
        tmp="";
        for (int j=0;j<26;j++){
            if (tu[i][j]==0) tmp=tmp+" ";
            else tmp=tmp+"*";
        }
        cout<<tmp<<endl;
    }
    for(int i=0;i<26;i++){
        char ch;ch='A'+i;
        cout<<ch;
    }


    return 0;
}

#include <iostream>
#include <cmath>
using namespace std;

int main(){
    //m t s;
    int m,t,s;
    int sheng;
    cin>>m>>t>>s;
    if(t==0){
        sheng=0;
        cout<<sheng<<endl;
        return 0;
        }
    int ch=ceil(s/t);
        sheng=m-ch;
    
    if (sheng<=0)
    	sheng=0;
    cout<<sheng<<endl;
    
    




    return 0;
}

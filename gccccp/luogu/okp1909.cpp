#include <iostream>
#include <cmath>
using namespace std;


int main(){
    //n; n1,j1; 
    int all;
    int n[3],j[3];
    int m[3];
    cin>>all;
    for (int i=0;i<3;i++){
       cin>>n[i]>>j[i];
        m[i]=ceil((all+0.0)/n[i])*j[i];
        
    }
   int min=m[0]; 
    for (int i=0;i<3;i++){
        if (m[i]<min) min=m[i];
    }
    cout<<min;
    
   
    
    return 0;
}

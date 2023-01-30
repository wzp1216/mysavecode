#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;


int main(){
  
    int n;
    cin>>n;
    float fei;
    if (n<=150)
        fei=n*0.4463;
    else if (n<=400)
        fei=150*0.4463+(n-150)*0.4663;
    else 
        fei=150*0.4463+(n-400)*0.5663+(400-150)*0.4663;
    cout<<std::fixed;
    cout<<std::setprecision(1)<<fei<<endl;

    
    return 0;
}

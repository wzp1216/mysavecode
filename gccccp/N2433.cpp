#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int n;
    cin>>n;
    int all=100;
        int r=5;double pi=3.141593;
    switch (n){
    case 1:
        cout<<"I love Luogu!"<<endl;
        break;
    case 2:
        cout<<"6 4"<<endl;
        break;
    case 3:
        cout<<3<<endl;
        cout<<12<<endl;
        cout<<2<<endl;
        break;
    case 4:
        cout.setf(ios::fixed);
        cout<<setprecision(2)<<500/3.0<<endl;
        break;
    case 5:
       cout<<15<<endl;
        break;
    case 6:
       cout<<10<<endl;
        break;
    case 7:
       while (all>=0) {
           all+=10;
           if (all>0) cout<<all<<endl; else cout<<0<<endl;
           all-=20;
           if (all>0) cout<<all<<endl; else cout<<0<<endl;
       }
        break;
    case 8:
        cout<<2*pi*r<<endl;
        cout<<pi*r*r<<endl;
        cout<<4*pi*r*r*r/3<<endl;
        break;
    case 9:
        cout<<15<<endl;
    default:
        break;

    }

    return 0;
}

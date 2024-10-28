#include <iostream>
using namespace std;
int main()
{
    std::cout << "Hello input:";
    int n;cin>>n;
    int wei=0,sum=0;
    int n_bak=n;
    while(n>=1){
        //取最后一位； sum*10+wei;
        wei=n%10;
        sum=sum*10+wei;
        cout<<n<<" "<<wei<<" "<<sum<<endl;
        n=n/10;
    }
    if (sum==n_bak) cout<<"回文"<<endl;
    else cout<<"no"<<endl;

    return 0;
}


#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;string st;
    cin>>n;cin>>st;
    while(n--){
        int mod,site_insert;cin>>mod;
        string str_app,st_insert,st_find;
        int a,b;
        switch (mod){
            case 1: 
                cin>>str_app;
                st.append(str_app);
                cout<<st<<endl;
                break;
            case 2: 
                cin>>a>>b;
                st=st.substr(a,b);
                cout<<st<<endl;
                break;
            case 3:
                cin>>site_insert;
                cin>>st_insert;
                st=st.insert(site_insert,st_insert);
                cout<<st<<endl;
                break;
            case 4:
                cin>>st_find;
                cout<<(int)st.find(st_find)<<endl;
                break;
            default:
                break;
        }

    }
    return 0;
}


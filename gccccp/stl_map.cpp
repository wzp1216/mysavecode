#include <iostream>
#include <map>
using namespace std;
int main(){
    std::map<char , int> foo,bar;
    foo['x']=100;
    foo['y']=200;
    bar['a']=11;
    bar['b']=22;
    bar['c']=33;
    foo.swap(bar);
    std::cout<<"foo:"<<std::endl;
    for (std::map<char,int>::iterator it=foo.begin();it!=foo.end();++it)
        cout<<it->first<<"-->"<<it->second<<endl;
    std::cout<<"bar:"<<std::endl;
    for (std::map<char,int>::iterator it=bar.begin();it!=bar.end();++it)
        cout<<it->first<<"-->"<<it->second<<endl;
    return 0;
}



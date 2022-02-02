
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

void printmap(map<int,string> &m)
{
    for(auto it:m)
    {cout<<it.first<<"-"<<it.second<<endl;
    }
}
    
void test01()
{
    map<int,string> m;
    m.insert(make_pair(10010,"ccc"));
    m.insert(make_pair(10086,"xxx"));
    m[2345]="wzp";
    printmap(m);
}



int main(){
    test01();
    return 0;
}

/*
int main(){
    vector<double> v;
    v.push_back(4);
    v.push_back(3.214);
    v.push_back(99.801);
    for (vector<double>::iterator iter=v.begin();iter!=v.end();++iter)
    cout<<*iter<<endl;
    cout<<"print v.at(2):"<<endl;
    cout<<v.at(2)<<endl;
    sort(v.begin(),v.end());
    
    for (auto a:v) cout<<a<<endl;
    return 0;
}
*/




/*
template <typename T>
T square(T x){
    return x*x;
}

template <typename T>
class Bovector{
    T arr[100];
    int size;
public:
    Bovector():size(0){}
    void push(T x){arr[size]=x;size++;}
    void print() const
    {
        for(int i=0;i<size;i++)
            cout<<arr[i]<<endl;
    }
};

int main(){
    int  a;
    a=5;
    cout<<square<int>(a)<<endl;
    cout<<square<double>(5.55)<<endl;

    Bovector<int> bv;
    bv.push(2);
    bv.push(8);
    bv.push(9);
    bv.push(7);
    bv.print();

    return 0;
}
*/


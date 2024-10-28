#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int main(){
    //a[3]  sort ;
    int l[3];
    cin>>l[0]>>l[1]>>l[2];

    vector<int> v(l,l+3);
    sort(v.begin(),v.end());
    int i=0;    
    for(auto it=v.begin();it!=v.end();++it){
        l[i]=*it;
        i++;
    }

    int a,b,c;
    a=l[0];b=l[1];c=l[2];
    //cout<<a<<b<<c<<endl;
    if ((a+b)<=c) cout<<"Not triangle"<<endl;
    if ((a*a+b*b)==(c*c))
        cout<<"Right triangle"<<endl;
    else if ((a*a+b*b)>(c*c))
        cout<<"Acute triangle"<<endl;
    else if ((a*a+b*b)<(c*c))
        cout<<"Obtuse triangle"<<endl;

    if ((a==b)||(b==c)) cout<<"Isosceles triangle"<<endl;
    if ((a==b)&&(b==c)) cout<<"Equilateral triangle"<<endl;
        
   
    
    return 0;
}

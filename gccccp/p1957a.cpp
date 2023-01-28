#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(){
	int a,b,c, n;
	cin>>n;
	cin.ignore();
	string st[n];
	string yout[n];
	char ch1,fuhao;
	stringstream ss;
	for (int i=0;i<n;i++){	
		getline(std::cin,st[i]);
		ch1=st[i][0];
		//cout<<ch1<<endl;
		ss<<st[i];
		if ((ch1>='a')&&(ch1<='c')) {
			ss>>fuhao>>a>>b;
		} else
			ss>>a>>b;
        ss.clear();
		if (fuhao=='a') {c=a+b;ss<<a<<"+"<<b;}
		else if (fuhao=='b') {c=a-b;ss<<a<<"-"<<b;}
		else if (fuhao=='c') {c=a*b;ss<<a<<"*"<<b;}
		ss>>yout[i];
        ss.clear();
		ss<<yout[i]<<"="<<c;
		ss>>yout[i];
        ss.clear();
		cout<<yout[i]<<endl;
		cout<<yout[i].size()<<endl;
	}
	
	return 0;
}


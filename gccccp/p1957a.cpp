#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(){
	int a,b,c, n;
	cin>>n;
	cin.get();
	string st[n];
	string yout[n];
	for (int i=0;i<n;i++){	
		getline(std::cin,st[i]);
	}
	char ch1,fuhao;
	stringstream ss,ss1;
	for (int i=0;i<n;i++){	
		ch1=st[i][0];
		//cout<<ch1<<endl;
		ss<<st[i];
		if ((ch1>='a')&&(ch1<='c')) {
			ss>>fuhao>>a>>b;
		} else
			ss>>a>>b;
		if (fuhao=='a') {c=a+b;ss1<<a<<"+"<<b;}
		else if (fuhao=='b') {c=a+b;ss1<<a<<"-"<<b;}
		else if (fuhao=='c') {c=a+b;ss1<<a<<"*"<<b;}
		ss1>>yout[i];
		ss<<yout[i]<<"="<<c;
		ss>>yout[i];
	}
	
	for (int i=0;i<n;i++){	
		cout<<yout[i]<<endl;
		cout<<yout[i].size()<<endl;
	}

	return 0;
}


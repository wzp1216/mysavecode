#include <iostream>
using namespace std;



















//################################################################
/*
#include <iostream>
using namespace std;
template <class T>
class mypair{
	T a,b;
	public:
	mypair(T  first,T second){
		a=first;b=second;
	}
	T getmax();
};

template <class T>
T mypair<T>::getmax()
{
	T res;
	res=a>b ? a: b;
	return res;
}

int main()
{
	mypair <int> myint(23,89);
	cout<<myint.getmax();
	return 0;
}
*/




//################################################################

/*
#include <iostream>
using namespace std;
template <class T>
T getmax(T a,T b)
{
	T res;
	res=(a>b)? a: b;
	return res;
}

int main()
{
	int i=2,j=5,k;
	double l=3.2,m=45.6,n;
	k=getmax<int>(i,j);
	n=getmax<double>(l,m);
	cout<<i<<"--"<<j<<"--"<<"max:"<<k<<endl;
	cout<<l<<"--"<<m<<"--"<<"max:"<<n<<endl;
	return 0;
}
*/





//################################################################
/*
#include <iostream>
using namespace std;
template <class T>
class mycontainer
{
	T element;
	public:
	mycontainer(T arg){element=arg;}
	T increase(){return ++element;}
};

//class template specialization:
template <>
class mycontainer <char>{
	char element;
	public:
	mycontainer(char arg){element=arg;}
	char uppercase()
	{
		if ((element>='a')&&(element<='z'))
			element+='A'-'a';
		return element;
	}
};


int main()
{
	mycontainer<int> myint(8);
	mycontainer<char> mychar('j');
	cout<<myint.increase()<<endl;
	//mychar.increase  is error!
	//cout<<mychar.increase()<<endl;
	cout<<mychar.uppercase()<<endl;
	return 0;
}
*/

//################################################################
/*
#include <iostream>
using namespace std;
template <class T, int N>
class mysequence
{
	T memblock [N];
	public:
	void setmember(int x,T value);
	T getmember(int x);
};

template <class T,int N>
void mysequence<T,N>::setmember(int x,T value){
	memblock[x]=value;
}

template <class T,int N>
T mysequence<T,N>::getmember(int x){
	return memblock[x];
}

int main()
{
	mysequence <int,5> myints ;
	mysequence <double,6> mydouble;
	myints.setmember(2,100);
	mydouble.setmember(3,8.9);
	cout<<myints.getmember(1)<<endl;
	cout<<myints.getmember(2)<<endl;
	cout<<mydouble.getmember(2)<<endl;
	cout<<mydouble.getmember(3)<<endl;
	return 0;
}
*/




/*
#include <iostream>
using namespace std;
template <class T>
T mymax(T a,T b){
	T c;
	c=(a>b)?a:b;
	return c;
}

int main()
{
	cout<<"mymax<int>(3,88)="<<mymax<int>(3,88)<<endl;
	cout<<"mymax<double>(2.3,5.6)="<<mymax<double>(2.3,5.6)<<endl;
	cout<<"mymax<char>=('a','k')="<<mymax<char>('a','k')<<endl;
	return 0;
}
*/
	


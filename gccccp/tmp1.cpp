#include <iostream>

template <class T>
T amax(T a, T b){
    return a<b?b:a;

}



int main()
{
    int x,y;
    std::cin>>x>>y;
    std::cout<<amax(x,y)<<std::endl;


    std::cout << "Hello world" << std::endl;
    return 0;
}


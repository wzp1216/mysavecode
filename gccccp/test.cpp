#include <iostream>
<<<<<<< HEAD
=======
#include <math>
>>>>>>> b24a16190fc6175294f270c1f425eeddb4b7f453

using namespace std;

int main()
{
<<<<<<< HEAD
    int y=6;
    std::cout<<"this is starting ..."<<std::endl;
    {
        int x;
        std::cout<<"x="<<x<<endl;
    }
    std::cout<<y;
=======
    int y{5};

    {
        int x;
        cin>>x;
        if (x==4) y=4;
    }
    cout<<y;
>>>>>>> b24a16190fc6175294f270c1f425eeddb4b7f453
    

    return 0;
}


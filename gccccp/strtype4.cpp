// strtype4.cpp -- line input
#include <iostream>
#include <string>               // make string class available
#include <cstring>              // C-style string library
int main()
{
    using namespace std;
    string str;
    getline(cin, str);          // cin now an argument; no length specifier
    cout << "You entered: " << str << endl;
    cout << "Length of string in str after input: "
         << str.size() << endl;
    for(int i=0;i<str.size();i++){
        cout<<str[i]<<endl;
    }

    // cin.get();

    return 0; 
}

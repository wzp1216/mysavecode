#include <string>
#include <iostream>
#include <cstdio>
#include <sstream>
using namespace std;
int main()
{
    // greet the user
    std::string name,line;
    std::cout << "What is your name? ";
    std::getline(std::cin, name);
    std::cout << "Hello " << name << ", nice to meet you.\n";

    //get length;
    cout<<"name is "<<name.size()<<endl;
    for (int i=0;i<name.size();i++) cout<<name[i]<<endl;
    // read file line by line
    int sum = 0;
    std::getline(std::cin,line);
    while(1){
    try{
         std::stoi(line);
    }
    catch (...) {
        break;
    }
        sum += std::stoi(line);
        std::getline(std::cin,line);
    }
    std::cout << "\nThe sum is " << sum << ".\n\n";

    return 0;
}
 

#include <string>
#include <iostream>
#include <cstdio>
#include <sstream>
int main()
{
    // greet the user
    std::string name,line;
    std::cout << "What is your name? ";
    std::getline(std::cin, name);
    std::cout << "Hello " << name << ", nice to meet you.\n";
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
 

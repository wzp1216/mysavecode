#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>

int main()
{
    for (int ch; (ch=std::getchar())!=EOF;)
    {
        if (std::isprint(ch))
            std::cout<<static_cast<char>(ch)<<'\n';
        if (ch==27)
            return EXIT_SUCCESS;
    }

    return EXIT_SUCCESS;
}
       

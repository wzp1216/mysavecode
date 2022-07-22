#include <unistd.h>
#include <stdlib.h>

int main()
{
    if ((write(1,"herei12345",10))!=10)
            write(2,"error",5);
    exit(0);

}

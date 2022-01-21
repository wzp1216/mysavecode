#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main()
{
    printf("the current process id is %d \n",getpid());
    printf("the father process id is %d \n",getppid());
    printf("the user true ID  is %d \n",getuid());
    printf("the valid user ID  is %d \n",geteuid());
    printf("the gruop id is %d \n",getgid());
    printf("the valid group id is %d \n",getegid());
    return 0;
}



#include <signal.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>
#define MAX 4096
static void sigalrm(int);
int main(void)
{
    int n;
    char line[MAX];
    if (signal(SIGALRM,sigalrm)==SIG_ERR)
        perror("signal(SIGALRM) error");
    alarm(2);
    if ((n=read(STDIN_FILENO,line,MAX))<0)
        perror("read error");
    alarm(0);
    write(STDOUT_FILENO,line,n);
    exit(0);
}
static void sigalrm(int signo) 
{
    printf("time is out; signal is %d \n",signo);
}



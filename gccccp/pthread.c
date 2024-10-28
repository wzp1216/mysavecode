#include <stddef.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
void print_msg(char *ptr);

int main(void)
{
    pthread_t thread1,thread2;
    int i,j;
    void *retval;
    char *msg1="this is the frist thread\n";
    char *msg2="this is second thread\n";
    pthread_create(&thread1,NULL,(void *)(&print_msg),(void *)msg1);
    pthread_create(&thread2,NULL,(void *)(&print_msg),(void *)msg2);
    pthread_join(thread1,&retval);
    pthread_join(thread2,&retval);
    return 0;
}
void print_msg(char *ptr)
{
    int i;
    for(i=0;i<10;i++)
        printf("%s",ptr);
}





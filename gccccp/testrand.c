#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    char s[64];
    int offset =0 ;
    int i;
    srand(time(0));
    for (i=0; i<10; i++)
    {
        offset+=sprintf(s+offset,"%d,",rand()%100);
    }
    s[offset-1]='\n';
    printf("%s",s);
    exit(0);
}



	

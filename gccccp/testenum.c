#include <stdio.h>

typedef enum {mon=1,tue,wed,thr,fri,sta,sun}weeks;

int main()
{
    weeks s;
    s=mon;
    while(s!=sun)
    {
        printf("%d",s);
        s++;
    }
    printf("%d\n",s);
    return 0;
}


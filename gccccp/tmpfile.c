#include <stdio.h>
#include <errno.h>
#include <stdlib.h>

int main()
{
    FILE *tempfp;
    char line[256];
    tempfp=tmpfile();
    if(tempfp ==NULL)
    {
        perror("tmpfile error1\n");
        return 1;
    }
    printf("opened a tmp file OK!\n");
    fputs("one line of data \n",tempfp);
    rewind(tempfp);
    if(fgets(line, sizeof(line),tempfp)==NULL)
    {
        printf("fgets error\n");
        return 2;
    }
    fputs(line,stdout);
    return 0;
}


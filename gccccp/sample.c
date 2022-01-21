#include <math.h>
#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>

char * make_message(const char *fmt, ...)
{
    int size=0;
    char *p=NULL;
    va_list ap;
    
    va_start(ap,fmt);
    size=vsnprintf(p,size,fmt,ap);
    va_end(ap);

    if (size<0)
        return NULL;
    size++;
    p=malloc(size);
    if(p==NULL)
        return NULL;
    va_start(ap,fmt);
    size=vsnprintf(p,size,fmt,ap);
    va_end(ap);
    if(size<0){
        free(p);
        return NULL;
    }
    return p;
}

int main()
{
    char* str = make_message("%d,%f,%s,%c",5,2.5,"test",'B');
    printf("%s\n",str);
    free(str);
    /* we allocate the memory in the make_message function, so we should release it by caller(main function). */
    return 0;
}

#include <stdio.h>
#include <string.h>
#include <strings.h>



typedef struct
{
    const char *data;
    int key;
}item;

item array[]={
    {"bill",3},
    {"neil",4},
    {"john",2},
    {"rick",5},
    {"alex",1},
};
int sort(item *a,int n)
{
    int s=0;
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(a[j].key<a[i].key)
            {
                item t=a[i];
                a[i]=a[j];
                a[j]=t;
                s++;
                printf("change times is %d \n",s);
            }
        }
    }
    return 0;
}



int main()
{
#ifdef DEGUG
    printf("Compiled: " __DATE__ " at " __TIME__" \n");
    printf("This is line %d of file %s \n.",__LINE__,__FILE__);
#endif
    printf("-----------------\n");

    int i;
    sort(array,5);
    for (i=0;i<5;i++){
        printf("array[%d]={%s,%d}\n",i,array[i].data,array[i].key);
    }
}

#include <stdarg.h>
#include <stdio.h>

double average(int num, ...)
{
    va_list arguments;//a arguments list;
    double sum=0;
    va_start(arguments,num);  //start
    for (int i=0;i<num;i++)
    {
        sum+=va_arg(arguments,double);//use
    }
    va_end(arguments);//end 
    return sum/num;
}
int main()
{
    printf("%f\n",average(3,12.1,12.3,11.8));
    printf("%f\n",average(5,3.1,12.3,11.8,2.2,1.1));
    return 0;
}



#include <stdio.h>


void PrintfText()
{
    printf("this is call back printf text\n");

}

void CallPrintText(void (*callfuct)())
{
    callfuct();

}
int main()
{
    CallPrintText(PrintfText);

    return 0;
}


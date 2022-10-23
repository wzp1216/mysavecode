#include <iostream>
#include <vector>

int main(){
    std::vector<int> myvector(10);

    for(int i=0;i<myvector.size();i++)
        myvector.at(i)=i;


    for(int i=0;i<myvector.size();i++)
        std::cout<<myvector.at(i);





    return 0;
}




/*
#include <stdio.h>
#include <assert.h>

void print_number(int *myint)
{
    if (myint!=NULL)    printf("%d\n",*myint);
    else printf("NULL\n");
}

int main(){
    int a=10;
    int *b=NULL;
    int *c=NULL;
    b=&a;
    print_number(b);
    print_number(c);
    return 0;
}
*/

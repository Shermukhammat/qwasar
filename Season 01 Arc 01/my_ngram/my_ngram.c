#include <stdio.h>
#include "mylib.h"

int main(int size, char *arr[])
{
    int data[127] = {0};
    
    datapro(size, arr, data);
    dataprint(data);
    
    return 0;
}
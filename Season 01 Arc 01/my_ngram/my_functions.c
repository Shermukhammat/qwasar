#include <stdio.h>
#include <string.h>

void datapro(int size, char **arr, int *data)
{
    int index = 0;
   
    for(int n = 1; n != size; n++)
    {
        // printf("%s\n", arr[n]);
        for(int i = 0; i != (int) strlen(arr[n]); i++)
        {
            // printf("%c ", arr[n][i]);
            index = arr[n][i];
            data[index] = data[index]+1;
        }
    }
}

void dataprint(int *data)
{
    for(int n = 0; n != 127; n++)
    {
        if(data[n] != 0)
        {
            printf("%c:%d\n", n, data[n]);
        }
    }
}
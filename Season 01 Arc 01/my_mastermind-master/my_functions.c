#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>

//FUNCTIONS FOR FUNCTIONS :)
int my_strlen(char* characters)
{
    int answer = 0;
    for(int z = 0; characters[z] != '\0'; z++)
    {
        answer++;
    }
    return answer;
}


char* my_random()
{
    char* answer=(char*)malloc(4*sizeof(char));
    srand(time(NULL));
	int n;
	start:
		for(int n = 0; n < 4; n++) answer[n] = (int) (rand() % 9) + 48;

		for(n = 0; n < 4; n++)
		{
			for(int z = n+1; z < 4; z++)
			{
				if(answer[n] == answer[z]) goto start;
			}
		}

    return answer;
}

//FOR THE MAIN FUNCTION
char* scode(int size, char **arr)
{
    char* answer = (char*) malloc(4 * sizeof(char));

    for(int n = 1; n != size; n++)
    {
        if(my_strlen(arr[n]) == 2 && arr[n][0] == '-' && arr[n][1] == 'c')
        {
            int count = 0;
            for(int i = 0; i != 4; i++)
            {                       
                if(arr[n+1][i] >= '0' && arr[n+1][i] <= '8') count++;
                else 
                {                               
                    answer = my_random();
                    return answer;
                }
            }

            if(count == 4)
            {
                for(int i = 0; i < 4; i++)
                {
                    answer[i] = arr[n+1][i];
                }
                return answer;
            }
            answer = my_random();
            return answer;
        }
    }
    answer = my_random();
    return answer;
}


int sycle(int size, char** arr)
{
    for(int n = 1; n != size; n++)
    {
        if(my_strlen(arr[n]) == 2)
        {
            if(arr[n][0] == '-' && arr[n][1] == 't')
            {
                return atoi(arr[n+1]);
            }
        }
    }
    return 10;
} 

int wellp(char* answer, char* correct_a)
{
    int count = 0;
    for(int n = 0; n != 4; n++)
    {
        if(answer[n] == correct_a[n])
        {
            count++;
        }
    }

    return count;
}


int misp(char* answer, char* correct_a)
{
    int count = 0;
    for (int i=0; i<4; i++) {
       for (int n=0; n<4; n++) 
        {
           if (correct_a[i] == answer[n] && i != n) count++;
        }
    }

    return count;
}


char* input()
{
    char* depo = (char*) malloc(4 * sizeof(char));
    char ram;
    int n = 0, sign;

    goto start;
        restart:
            write(0, "Wrong input!\n", 13);          

            start:
                ram = ' ';
                write(0, ">", 1);
                for(n = 0; ram != '\n'; n++)
                {
                    sign = read(0,&ram,1);
                    if(sign == 0) exit(1);
                    if(n < 4) depo[n] = ram;                
                }
                if(n != 5) goto restart;
                
                for(int i = 0; i != 4; i++)
                {
                    if(depo[i] >= '0' && depo[i] <= '8') {}
                    else goto restart;
                }

                for(int n = 1; n < 4; n++)
                {
                    for(int z = n; z != 0; z--)
                    {
                        if(depo[n] == depo[z-1]) goto restart;
                    }
                }

    return depo;  
}
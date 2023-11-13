#ifndef MY_FUNCTIONS
#define MY_FUNCTIONS
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

char* scode(int size, char **arr);

int sycle(int size, char** arr);

int wellp(char* answer, char* correct_a);

int misp(char* answer, char* correct_a);

char* input();

#endif
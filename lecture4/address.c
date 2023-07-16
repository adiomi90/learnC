#include <stdio.h>
#include <string.h>

int main(void)
{
    char *n = "HI!";
    char *y = "HI!";

    if(strcmp(n, y) ==  0)
    {
        printf("Same");
    }
    else
    {
        printf("Different");
    }
}